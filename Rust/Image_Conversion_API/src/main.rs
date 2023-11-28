use actix_web::{web, App, HttpResponse, HttpServer, Responder};
use actix_web::web::Bytes;
use image::{DynamicImage, GenericImageView, ImageFormat};
use std::io::{Cursor, Write};

fn convert_image(data: Bytes, format: &str) -> impl Responder {
    // Convert bytes to DynamicImage
    let img = image::load_from_memory(&data).map_err(|e| {
        HttpResponse::BadRequest().body(format!("Error loading image: {}", e))
    });

    // Convert DynamicImage to the desired format
    let result = img.and_then(|img| {
        // Convert to bytes in the specified format
        let mut output_data = Vec::new();
        let mut cursor = Cursor::new(&mut output_data);

        match format.to_lowercase().as_str() {
            "jpeg" => {
                // Adjust the quality setting as needed (0 to 100)
                img.write_to(&mut cursor, image::ImageOutputFormat::Jpeg(85))
                    .map_err(|e| HttpResponse::InternalServerError().body(format!("Error converting image: {}", e)))?;
            }
            "png" => {
                img.write_to(&mut cursor, image::ImageOutputFormat::Png)
                    .map_err(|e| HttpResponse::InternalServerError().body(format!("Error converting image: {}", e)))?;
            }
            "gif" => {
                img.write_to(&mut cursor, image::ImageOutputFormat::Gif)
                    .map_err(|e| HttpResponse::InternalServerError().body(format!("Error converting image: {}", e)))?;
            }
            "bmp" => {
                img.write_to(&mut cursor, image::ImageOutputFormat::Bmp)
                    .map_err(|e| HttpResponse::InternalServerError().body(format!("Error converting image: {}", e)))?;
            }
            _ => {
                return Err(HttpResponse::BadRequest().body("Unsupported image format"));
            }
        }

        Ok(output_data)
    });

    match result {
        Ok(output_data) => HttpResponse::Ok().body(output_data),
        Err(response) => response,
    }
}

async fn convert_image_handler(data: Bytes, format: web::Path<String>) -> impl Responder {
    convert_image(data, &format)
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .app_data(web::PayloadConfig::default().limit(1024 * 1024 * 10)) // Set payload limit to 10 MB
            .route("/convert/{format}", web::post().to(convert_image_handler))
    })
    .bind("127.0.0.1:8080")?
    .run()
    .await
}

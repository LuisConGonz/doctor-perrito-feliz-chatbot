
 Doctor Perrito Feliz - ChatBot de Adopciones

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Documentation](https://img.shields.io/badge/docs-ReadTheDocs-blue)](https://doctor-perrito-feliz.readthedocs.io)

Descripcion
Doctor Perrito Feliz - ChatBot de Adopciones

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Documentation](https://img.shields.io/badge/docs-ReadTheDocs-blue)](https://doctor-perrito-feliz.readthedocs.io)

Descripción
ChatBot para facilitar adopciones animales en refugios sin fines de lucro, automatizando consultas frecuentes en WhatsApp/Facebook.

Problema Identificado
- Sobrecarga del personal respondiendo preguntas repetitivas
- 70% de consultas son sobre requisitos y disponibilidad de mascotas
- Proceso de adopción manual y lento

Solución
- ChatBot 24/7 con respuestas automáticas
- Integración con redes sociales
- Panel de administración para actualizar datos

 Arquitectura
```mermaid
graph TD
    A[Usuario] --> B[WhatsApp/Facebook]
    B --> C[ChatBot Python]
    C --> D[(SQLite/PostgreSQL)]
    C --> E[Panel Admin Flask]                                                                                     Licencia MIT - © 2023 Doctor Perrito Feliz

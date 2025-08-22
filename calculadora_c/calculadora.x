struct float_array {
    float vector[1000];
    int tam;
};

struct float_matrix {
    float m[1000];
    int tam1;
    int tam2;
};

program CALCULADORA{
    version CALC{
        float SUMA (float a, float b) = 1; /* Número de procedimiento */
        float MULTIPLICACION (float a, float b) = 2;
        float RESTA (float a, float b) = 3;
        float DIVISION (float a, float b) = 4;
        float SENO (float a) = 5;
        float COSENO (float a) = 6;
        float TANGENTE (float a) = 7;
        float ARCOSENO (float a) = 8;
        float ARCOCOSENO (float a) = 9;
        float ARCOTANGENTE (float a) = 10;
        float RAIZ_CUADRADA (float a) = 11;
        float POTENCIA (float a, float b) = 12;
        float_array SUMA_VECTORES (float_array a, float_array b) = 13;
        float_array RESTA_VECTORES (float_array a, float_array b) = 14;
        float PRODUCTO_ESCALAR (float_array a, float_array b) = 15;
        float_array PRODUCTO_VECTORIAL (float_array a, float_array b) = 16;
        float_matrix SUMA_MATRICES (float_matrix a, float_matrix b) = 17;
        float_matrix RESTA_MATRICES (float_matrix a, float_matrix b) = 18;
        float_matrix MULTIPLICACION_MATRICES (float_matrix a, float_matrix b) = 19;
        float_matrix DIVISION_MATRIZ_REAL (float_matrix a, float b) = 20;
    } = 1; /* Número de versión */
} = 0x20000541; /* Número del programa */

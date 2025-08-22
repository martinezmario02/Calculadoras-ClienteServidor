service Calculadora{
   void ping(),
   
   double suma(1:double num1, 2:double num2),
   double resta(1:double num1, 2:double num2),
   double producto(1:double num1, 2:double num2),
   double division(1:double num1, 2:double num2),

   double seno(1:double num),
   double coseno(1:double num),
   double tangente(1:double num),
   double arcoseno(1:double num),
   double arcocoseno(1:double num),
   double arcotangente(1:double num),

   double raiz_cuadrada(1:double num),
   double potencia(1:double num1, 2:double num2),
   double logaritmo(1:double num1, 2:double num2),
   double porcentaje(1:double num1, 2:double num2),
   double modulo(1:double num1, 2:double num2),

   list<double> suma_vectores(1:list<double> v1, 2:list<double> v2),
   list<double> resta_vectores(1:list<double> v1, 2:list<double> v2),
   double producto_escalar(1:list<double> v1, 2:list<double> v2),
   list<double> producto_vectorial(1:list<double> v1, 2:list<double> v2),
   list<double> division_vector_real(1:list<double> v1, 2:double num),

   list<list<double>> suma_matrices(1:list<list<double>> m1, 2: list<list<double>> m2),
   list<list<double>> resta_matrices(1:list<list<double>> m1, 2: list<list<double>> m2),
   list<list<double>> multiplicacion_matrices(1:list<list<double>> m1, 2: list<list<double>> m2),
   list<list<double>> division_matriz_real(1:list<list<double>> m1, 2: double m2),
}

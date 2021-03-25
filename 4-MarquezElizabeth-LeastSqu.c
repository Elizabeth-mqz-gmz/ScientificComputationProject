/*      Elizabeth Marquez Gomez
       Computo Cientifico 2020-2
            Generacion 17
  Licenciatura en Ciencias Genomicas
Universidad Nacional Autonoma de Mexico */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// FUNCTION TO OBTAIN THE SUM OF VARIOUS NUMBERS, WHICH CAN BE RAISED TO ANY NUMBER IF REQUIRED
float GetSum(int num, float *vec, int type, int power){
  float sum = 0;
  for(int counter=0; counter<num; counter++){
    if(type == 0)
      sum += *(vec+counter);
    // INDICATES IF IT'S REQUIRED AND TO RAISE THE VALUES
    if(type == 1)
      sum += pow(*(vec+counter),power);
  }
  return sum;
}
// FUNCTION TO CLEAN UP THE MATRIX OF VALUES
void CleanUpMatrix(float **matrix, int num) {
  if(matrix){
    for (int counter = 0; counter <= num; counter++)
      if(*(matrix+counter)){
        free(*(matrix+counter));
        *(matrix+counter) = NULL;
      }
    free(matrix);
    matrix = NULL;
  }
}
// FUNCTION TO CLEAN POINTER VECTORS
void CleanBasic(float *vec){
  free(vec);
  vec = NULL;
}
// FUNCTION TO PRINT THE MATRIX AND VALUES OF Y
void PrintSystem(int degree, float **matrix, float *results){
  printf("\n");
  for (int i = 0; i <=degree; i++) {
    for (int j = 0; j <=degree; j++)
      printf("%f\t", matrix[i][j]);
    printf("|\t%f\n", results[i]);
  }
}
//------------------------------------------------------------------------------------------------------------------------
int main() {
  int numPoints = 0, degree = 0, i = 0, j = 0, k = 0, l = 0, external = 0, internal = 0, mInt = 0, index = 0, jump;
  float *vecX=NULL, *vecY=NULL, aux = 0, complementY, **mat, *results=NULL, divider = 0;

  printf("\t\t-- Welcome to Least Squares method --");
  printf("\n-> Insert the number of points to fit the line: ");
  scanf("%d", &numPoints);
  printf("\n-> Insert the degree for the polynomial: ");
  scanf("%d", &degree);

  // RESERVE SPACE FOR vecX AND vecY
  if(!(vecX = (float*)calloc(numPoints, sizeof(float))) || !(vecY = (float*)calloc(numPoints, sizeof(float)))){
    printf("\nERROR: We could not reserve space to save X and Y values, sorry :(\n");
    CleanBasic(vecX);
    CleanBasic(vecY);
    exit(1);
  }
  // FILL THE VECTORS WITH POINT VALUES
  for(i=0; i<numPoints; i++){
    printf("\nInsert value for X%d: ", i+1);
    scanf("%f", &aux);
    *(vecX+i) = aux;

    printf("\nInsert value for Y%d: ", i+1);
    scanf("%f", &aux);
    *(vecY+i) = aux;
  }

  // RESERVE SPACE FOR VECTOR OF RESULT OF THE SYSTEM
  if(!(results = (float*)calloc(degree+1, sizeof(float)))){
    printf("\nERROR: We could not reserve space save the results, sorry :(\n");
    CleanBasic(vecX);
    CleanBasic(vecY);
    CleanBasic(results);
    exit(1);
  }
  // RESERVE SPACE FOR SYSTEM OF EQUATIONS MATRIX (principal vector)
  mat = (float**)calloc(degree+1, sizeof(float*));
  if(mat == NULL){
    printf("\nERROR: We could not reserve space save the system of equations, sorry :(\n");
    CleanBasic(vecX);
    CleanBasic(vecY);
    CleanBasic(results);
    CleanUpMatrix(mat, degree);
    exit(1);
  }
  // RESERVE SPACE FOR SYSTEM OF EQUATIONS MATRIX (secondary vectors)
  for (i = 0; i <= degree; i++) {
    mat[i] = (float*)calloc(degree+1, sizeof(float));
    if(mat == NULL){
      printf("\nERROR: We could not reserve space save the system of equations, sorry :(\n");
      CleanBasic(vecX);
      CleanBasic(vecY);
      CleanBasic(results);
      CleanUpMatrix(mat, degree);
      exit(1);
    }
  }
  // FILL MATRIX WITH INTERPRETED VALUES OF X AND Y
  for(external=0; external<=degree; external++){ // 0 -> degree //0->1, 1->1
    mInt = degree+external; // mInt = degree + external // 1, 2
    for(internal = external; internal <= mInt; internal++){ // external -> mInt // 0->1, 1->2
      if(external == 0 && internal == 0)
        mat[0][0] = numPoints;
      else
        mat[external][internal-external] = GetSum(numPoints, vecX, 1, internal);
    }
    complementY = 0;
    for(i=0; i<numPoints; i++)
      complementY += pow(*(vecX+i),external) * (*(vecY+i));

    results[external] = (external == 0) ? GetSum(numPoints, vecY, 0, 0) : complementY;
  }
  // PRINT SYSTEM
  printf("\n\tWe have obtained this system of equations");
  PrintSystem(degree, mat, results);

  //START TO SOLVE THE SYSTEMN OF EQUATIONS USING GAUSS-JORDAN METHOD
  // GET DIAGONAL OF 1
  for (i = 0; i <= degree; i++) {
    divider = mat[i][i];
    for (j = 0; j <= degree; j++)
      mat[i][j] /= divider;
    results[i] /= divider;

    for (k = i+1; k <= degree; k++) {
      aux = mat[k][i];
      for(l = 0; l <= degree; l++)
        mat[k][l] -= mat[i][l] * aux;
      results[k] -= results[i] * aux;
    }
  }
  // SOLVE UPPER DIAGONAL MATRIX
  jump = 1;
  for(i=0; i<degree; i++){
    index = (degree-1) - i;
    for(j=0; j<=index; j++){
      aux = mat[j][j+jump];
      for(k = j+jump; k<= degree; k++)
          mat[j][k] -= mat[j+jump][k] * aux;
      results[j] -= results[j+jump] * aux;
    }
    jump++;
  }
  //PRINT SYSTEM SOLVED
  printf("\n\tSystem of equations solved");
  PrintSystem(degree, mat, results);
  printf("\n\tY = ");
  for (i = 0; i <= degree; i++) {
    if(i < 2){
      if(i == 0)
        printf("%f ", results[i]);
      else
        printf("+ %fx ", results[i]);
    }
    else
      printf("+ %fx^%d", results[i],i);
  }
  printf("\n");
  //FREE ALL
  CleanBasic(vecX);
  CleanBasic(vecY);
  CleanBasic(results);
  CleanUpMatrix(mat, degree);
  return 0;
}
/*            +----MAIN----+
*NAME*         *TYPE*           *USAGE*
numPoints       int             Indicates the dimension of the vector to save points
degree          int             Indicates the dimension for matrix and results vector
i, j, k, l      int             Indicates the iteration inside the for
external        int             Controls the external for to solve the system
internal        int             Controls the internal for to solve the system
mInt            int             Saves an special number that indicates the maximum value inside the internal for
index           int             Saves an special number that indicates the index to use to solve upper diagonal matrix
jump            int             Indicates the jump number to solve upper diagonal matrix
vecX    pointer vector, float   Is the vector to save X values
vecY    pointer vector, float   Is the vector to save Y values
aux            float            Saves temporary values
complementY    float            Saves the sum to add to Y sum
mat     matrix vector, float    Is the matrix to save system
results  pointer vector, float  Is the vector to save result values for each equation
divider        float            Indicates the value that will be used to divide the others
              +----GetSum----+
*NAME*         *TYPE*           *USAGE*
num             int             Indicates the dimension of the vector
vec    pointer vector, float    Indicates the vector to read values
type            int             Indicates the type of method to use
power           int             Indicates the number to raise values
sum             float           It saves the sum of values that will be returned
counter         int             Indicates the iteration inside the for
              +----CleanUpMatrix----+
*NAME*         *TYPE*           *USAGE*
matrix   matrix vector, float   Indicates the matrix to clean up
num             int             Indicates the dimension of the matrix
counter         int             Indicates the iteration inside the for
              +----CleanBasic----+
*NAME*         *TYPE*           *USAGE*
vec    pointer vector, float    Indicates the vector to clean up
              +----PrintSystem----+
*NAME*         *TYPE*            *USAGE*
degree         int               Indicates dimension of matrix and vector
matrix    matrix vector, float   Indicates the matrix to print
results   pointer vector, float  Indicates the vector to print
i, j           int               Indicates the iteration inside the for
*/

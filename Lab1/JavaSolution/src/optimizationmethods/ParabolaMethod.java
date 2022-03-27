package optimizationmethods;

import static optimizationmethods.MyFunc.myFunc;

public class ParabolaMethod {
    private static double findX(double x1, double x2, double x3, double f1, double f2, double f3){
        double numerator = Math.pow(x2 - x1, 2)*(f2 - f3) - Math.pow(x2 - x3, 2)*(f2 - f1);
        double denominator = 2*((x2 - x1)*(f2 - f3) - (x2 - x3)*(f2 - f1));
        return x2 - numerator / denominator;
    }

    public static double parabola(double eps, double x1, double x3){
        double x2 = (x1 + x3) / 2;
        double funcValue1 = myFunc(x1);
        double funcValue2 = myFunc(x2);
        double funcValue3 = myFunc(x3);
        double u;
        double funcValueU;
        while(x3 - x1 > eps){
            u = findX(x1, x2, x3, funcValue1, funcValue2, funcValue3);
            funcValueU = myFunc(u);
            if(x2 <= u) {
                if(funcValue2 <= funcValueU){
                    x3 = u;
                    funcValue3 = funcValueU;
                }
                else{
                    x1 = x2;
                    x2 = u;
                    funcValue1 = funcValue2;
                    funcValue2 = funcValueU;
                }
            }
            else{
                if(funcValueU <= funcValue2){
                    x3 = x2;
                    x2 = u;
                    funcValue2 = funcValueU;
                    funcValue3 = funcValue2;
                }
                else{
                    x1 = u;
                    funcValue1 = funcValueU;
                }
            }
        }
        return (x1 + x3) / 2;
    }
}

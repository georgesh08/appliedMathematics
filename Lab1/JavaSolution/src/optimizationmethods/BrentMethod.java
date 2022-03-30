package optimizationmethods;

import static optimizationmethods.MyFunc.myFunc;

public class BrentMethod {
    private static double findU(double x1, double x2, double x3, double f1, double f2, double f3) {
        double numerator = Math.pow(x2 - x1, 2) * (f2 - f3) - Math.pow(x2 - x3, 2) * (f2 - f1);
        double denominator = 2 * ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1));
        return x2 - numerator / denominator;
    }

    public static double brent(double eps, double a, double c) {
        double k = (3 - Math.sqrt(5)) / 2;
        double x = (a + c) / 2;
        double fx = myFunc(x);
        double w = x, v = x;
        double fw = fx, fv = fx;
        double d = c - a;
        double e = d;
        double g;
        double u = 0, fu;
        double counter = 0, funcCalls = 1;
        while (c - a > eps) {
            counter++;
            g = e;
            e = d;
            if (x != w && w != v && x != v && fx != fv && fx != fw && fw != fv) {
                u = findU(x, w, v, fx, fw, fv);
            }
            if (u >= a + eps && u <= c - eps && Math.abs(u - x) < g / 2) {
                d = Math.abs(u - x);
            } else {
                if (x < (c - a) / 2) {
                    u = x + k * (c - x);
                    d = c - x;
                } else {
                    u = x - k * (x - a);
                    d = x - a;
                }
            }
            fu = myFunc(u);
            funcCalls++;
            if (fu <= fx) {
                if (u >= x) {
                    a = x;
                } else {
                    c = x;
                }
                v = w;
                w = x;
                x = u;
                fv = fw;
                fw = fx;
                fx = fu;
            } else {
                if (u >= x) {
                    c = u;
                } else {
                    a = u;
                }
                if (fu <= fw || w == x) {
                    v = w;
                    w = u;
                    fv = fw;
                    fw = fu;
                } else if (fu <= fv || v == x || v == w) {
                    v = u;
                    fv = fu;
                }
            }
        }
        System.out.println("\nBrent iterations: " + counter + "\nFunc calls: " + funcCalls + "\n");
        return (a + c)/2;
    }
}

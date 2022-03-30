package optimizationmethods;

import static optimizationmethods.MyFunc.myFunc;

public class GoldenRatioMethod {
    private static final double phi = (3 - Math.sqrt(5))/2;

    private static double countX1(double lowerBound, double upperBound){
        return lowerBound + phi * (upperBound - lowerBound);
    }

    private static double countX2(double lowerBound, double upperBound){
        return upperBound - phi * (upperBound - lowerBound);
    }

    public static double goldenRatio(double eps, double lowerBound, double upperBound){
        double counter = 0, prev = 1, funcCalls = 2;
        double x1 = countX1(lowerBound, upperBound);
        double x2 = countX2(lowerBound, upperBound);
        double funcValue1 = myFunc(x1);
        double funcValue2 = myFunc(x2);
        System.out.println("Golden ratio:");
        while(upperBound - lowerBound > eps){
            System.out.println(counter++ + " | " + Math.abs(upperBound - lowerBound) + " | "
                    + Math.abs(upperBound - lowerBound)/prev);
            prev = Math.abs(upperBound - lowerBound);
            if(funcValue2 > funcValue1){
                upperBound = x2;
                x2 = x1;
                x1 = countX1(lowerBound, upperBound);
                funcValue2 = funcValue1;
                funcValue1 = myFunc(x1);
                funcCalls++;
            } else if(funcValue1 > funcValue2) {
                lowerBound = x1;
                x1 = x2;
                x2 = countX2(lowerBound, upperBound);
                funcValue1 = funcValue2;
                funcValue2 = myFunc(x2);
                funcCalls++;
            }
        }
        System.out.println("\nGolden ratio iterations: " + counter + "\nFunc calls: " + funcCalls + "\n");
        return (upperBound + lowerBound)/2;
    }
}

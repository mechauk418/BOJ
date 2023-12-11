import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        int[] a = new int[n];

        for (int i=0; i<n; i++) {
            a[i]=sc.nextInt();

        }

        int[] b = new int[n];

        for (int i=0; i<n; i++) {
            b[i]=1;

        }

        for (int i=1; i<n; i++) {
            for (int j=0; j<i; j++) {
                if (a[i]<a[j]) {
                    b[i] = Math.max(b[j]+1,b[i]);
                }

            }
        }
        int maxAns = Arrays.stream(b).max().getAsInt();
        System.out.println(maxAns);
    }
}
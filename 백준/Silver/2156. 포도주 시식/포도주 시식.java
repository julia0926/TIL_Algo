import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr=new int[n+1];
        int[] dp=new int[n+1]; //이전 잔들을 선택한 최대 합

        for(int i=1;i<=n;i++){
            arr[i]=sc.nextInt();
        }
        //Bottom-up 방식으로 품 (작은것부터 끝까지)
        dp[1] = arr[1]; //1개 자체가 최대 값
        if(n>1){
            dp[2] = arr[1]+arr[2]; //1, 2번째 값
        }
        for(int i=3;i<=n;i++){
            dp[i]=Math.max(dp[i-1], Math.max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i]));
            /*
            dp[3]=Math.max(dp[2] , Math.max(dp[1] + arr[3], dp[0] + arr[2] + arr[3] ));
            (1,2) vs (1,3) vs (2,3) 비교하는 것과 같음
                => (2,3) = 23
            dp[4]=Math.max(dp[3] , Math.max(dp[2] + arr[4], dp[1] + arr[3] + arr[4] ));
            (2,3) vs (1,2,4) vs (1,3,4)
                => (1,3,4) = 28
            dp[5]=Math.max(dp[4] , Math.max(dp[3] + arr[5], dp[2] + arr[4] + arr[5] ));
            (1,3,4) vs (2,3,5) vs (1,2,4,5)
                => (1,2,4,5) = 33
            dp[6]=Math.max(dp[5] , Math.max(dp[4] + arr[6], dp[3] + arr[5] + arr[6] ));
            (1,2,4,5) vs (1,3,4,6) vs (2,3,5,6)
                => (1,2,4,5) = 33
             */

        }
        System.out.println(dp[n]);
    }
}

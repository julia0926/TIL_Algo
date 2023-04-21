
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    static int[] visited = new int[100001]; //이동 경로? 방문경로?

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int k=sc.nextInt();
        move(n,k);
    }

    public static void move(int n, int k) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(n); //처음 값 n을 넣음 !

        while (!q.isEmpty()) {
            int value = q.poll();//큐에 있는 제일 첫번째 값을 꺼냄
            if(value==k) {
                System.out.println(visited[k]);
                break;
            }
            if(value>0&&visited[value-1]==0){
                q.offer(value-1);
                visited[value-1]=visited[value]+1;
            }if(value<100000&&visited[value+1]==0){
                q.offer(value+1);
                visited[value+1]=visited[value]+1;
            }if(value*2<=100000&&visited[value*2]==0){
                q.offer(value*2);
                visited[value*2]=visited[value]+1;
            }
        }
    }

}



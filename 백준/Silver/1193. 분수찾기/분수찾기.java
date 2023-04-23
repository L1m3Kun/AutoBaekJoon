import java.io.*;

class Main{
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        if(N==1) System.out.println(1+"/"+1);
        else{
        int start = 0, end =1, i=1;
        while(end < N){
            i++;
            start = end+1;
            end += i;
        }
        if(i%2==0) System.out.println((N-start+1)+"/"+(i-N+start));
        else System.out.println((i-N+start)+"/"+(N-start+1));
        }
    }
}
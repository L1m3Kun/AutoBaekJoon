import java.io.*;

class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] str = br.readLine().split("");
        char[] alpha = new char[26];
        int[] ans = new int[26];
        for(int i=0;i<26;i++){
            alpha[i] = (char)(97+i);
            ans[i] = -1;
        }
        for(int i=0;i<str.length;i++){
            for(int j=0;j<26;j++){
                if(str[i].equals(Character.toString(alpha[j])) && ans[j]==-1){
                    ans[j] = i;
                }
            }
        }
        for(int i=0;i<26;i++) bw.write(String.valueOf(ans[i]+" "));
        bw.flush();
    }
}
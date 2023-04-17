// 25206 너의 평점은
import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        double score = 0.0;
        int total = 0;
        String[] str;
        for(int i=0;i<20;i++){
            str = br.readLine().split(" ");
            if(str[2].equals("A+")){
                if(str[1].equals("4.0")){
                    score += 4.5 * 4.0;
                    total += 4;
                }
                else if (str[1].equals("3.0")){
                    score += 4.5 * 3.0;
                    total += 3;
                }
                else if (str[1].equals("2.0")){
                    score += 4.5 * 2.0;
                    total += 2;
                }
                else if (str[1].equals("1.0")){
                    score += 4.5 * 1.0;
                    total += 1;
                }


            }
            else if(str[2].equals("A0")){
                if(str[1].equals("4.0")){
                    score += 4.0 * 4.0;
                    total += 4;
                }
                else if (str[1].equals("3.0")){
                    score += 4.0 * 3.0;
                    total += 3;
                }
                else if (str[1].equals("2.0")){
                    score += 4.0 * 2.0;
                    total += 2;
                }
                else if (str[1].equals("1.0")){
                    score += 4.0 * 1.0;
                    total += 1;
                }

            }
            else if(str[2].equals("B+")){
                if(str[1].equals("4.0")){
                    score += 3.5 * 4.0;
                    total += 4;
                }
                else if (str[1].equals("3.0")){
                    score += 3.5 * 3.0;
                    total += 3;
                }
                else if (str[1].equals("2.0")){
                    score += 3.5 * 2.0;
                    total += 2;
                }
                else if (str[1].equals("1.0")){
                    score += 3.5 * 1.0;
                    total += 1;
                }

            }
            else if(str[2].equals("B0")){
                if(str[1].equals("4.0")){
                    score += 3.0 * 4.0;
                    total += 4;
                }
                else if (str[1].equals("3.0")){
                    score += 3.0 * 3.0;
                    total += 3;
                }
                else if (str[1].equals("2.0")){
                    score += 3.0 * 2.0;
                    total += 2;
                }
                else if (str[1].equals("1.0")){
                    score += 3.0 * 1.0;
                    total += 1;
                }
            }
            else if(str[2].equals("C+")){
                if(str[1].equals("4.0")){
                    score += 2.5 * 4.0;
                    total += 4;
                }
                else if (str[1].equals("3.0")){
                    score += 2.5 * 3.0;
                    total += 3;
                }
                else if (str[1].equals("2.0")){
                    score += 2.5 * 2.0;
                    total += 2;
                }
                else if (str[1].equals("1.0")){
                    score += 2.5 * 1.0;
                    total += 1;
                }

            }
            else if(str[2].equals("C0")){
                if(str[1].equals("4.0")){
                    score += 2.0 * 4.0;
                    total += 4;
                }
                else if (str[1].equals("3.0")){
                    score += 2.0 * 3.0;
                    total += 3;
                }
                else if (str[1].equals("2.0")){
                    score += 2.0 * 2.0;
                    total += 2;
                }
                else if (str[1].equals("1.0")){
                    score += 2.0 * 1.0;
                    total += 1;
                }

            }
            else if(str[2].equals("D+")){
                if(str[1].equals("4.0")){
                    score += 1.5 * 4.0;
                    total += 4;
                }
                else if (str[1].equals("3.0")){
                    score += 1.5 * 3.0;
                    total += 3;
                }
                else if (str[1].equals("2.0")){
                    score += 1.5 * 2.0;
                    total += 2;
                }
                else if (str[1].equals("1.0")){
                    score += 1.5 * 1.0;
                    total += 1;
                }

            }
            else if(str[2].equals("D0")){
                if(str[1].equals("4.0")){
                    score += 1.0 * 4.0;
                    total += 4;
                }
                else if (str[1].equals("3.0")){
                    score += 1.0 * 3.0;
                    total += 3;
                }
                else if (str[1].equals("2.0")){
                    score += 1.0 * 2.0;
                    total += 2;
                }
                else if (str[1].equals("1.0")){
                    score += 1.0 * 1.0;
                    total += 1;
                }
            }
            else if(str[2].equals("F")){
                if(str[1].equals("4.0")){
                    total += 4;
                }
                else if (str[1].equals("3.0")){
                    total += 3;
                }
                else if (str[1].equals("2.0")){
                    total += 2;
                }
                else if (str[1].equals("1.0")){
                    total += 1;
                }
            }

        }

        bw.write(String.valueOf(score/total));
        bw.flush();
    }
}
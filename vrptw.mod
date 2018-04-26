/*********************************************
 * OPL 12.6.3.0 Model
 * Author: hedge
 * Creation Date: 2018-4-26 at 上午9:19:22
 *********************************************/
int tot=12;
range I=0..tot+1;//I is the terminal
range K=1..6;//K is the driver

//====================================================================
//coordinate======= [[9, 4], [13, 8], [11, 2], [4, 10], [6, 12], [6, 5], [2, 10], [13, 8], [3, 2], [11, 10], [4, 3], [2, 13]]
float arrive_time[I]= [0, 38, 34, 51, 19, 5, 19, 32, 37, 26, 11, 39, 17, 0] ;

float distance[0..tot+1][0..tot+1]=[
[ 0 , 9.85 , 15.26 , 11.18 , 10.77 , 13.42 , 7.81 , 10.2 , 15.26 , 3.61 , 14.87 , 5.0 , 13.15 , 0],
[ 0 , 0.0 , 5.66 , 2.83 , 7.81 , 8.54 , 3.16 , 9.22 , 5.66 , 6.32 , 6.32 , 5.1 , 11.4 , 0],
[ 0 , 5.66 , 0.0 , 6.32 , 9.22 , 8.06 , 7.62 , 11.18 , 0.0 , 11.66 , 2.83 , 10.3 , 12.08 , 0],
[ 0 , 2.83 , 6.32 , 0.0 , 10.63 , 11.18 , 5.83 , 12.04 , 6.32 , 8.0 , 8.0 , 7.07 , 14.21 , 0],
[ 0 , 7.81 , 9.22 , 10.63 , 0.0 , 2.83 , 5.39 , 2.0 , 9.22 , 8.06 , 7.0 , 7.0 , 3.61 , 0],
[ 0 , 8.54 , 8.06 , 11.18 , 2.83 , 0.0 , 7.0 , 4.47 , 8.06 , 10.44 , 5.39 , 9.22 , 4.12 , 0],
[ 0 , 3.16 , 7.62 , 5.83 , 5.39 , 7.0 , 0.0 , 6.4 , 7.62 , 4.24 , 7.07 , 2.83 , 8.94 , 0],
[ 0 , 9.22 , 11.18 , 12.04 , 2.0 , 4.47 , 6.4 , 0.0 , 11.18 , 8.06 , 9.0 , 7.28 , 3.0 , 0],
[ 0 , 5.66 , 0.0 , 6.32 , 9.22 , 8.06 , 7.62 , 11.18 , 0.0 , 11.66 , 2.83 , 10.3 , 12.08 , 0],
[ 0 , 6.32 , 11.66 , 8.0 , 8.06 , 10.44 , 4.24 , 8.06 , 11.66 , 0.0 , 11.31 , 1.41 , 11.05 , 0],
[ 0 , 6.32 , 2.83 , 8.0 , 7.0 , 5.39 , 7.07 , 9.0 , 2.83 , 11.31 , 0.0 , 9.9 , 9.49 , 0],
[ 0 , 5.1 , 10.3 , 7.07 , 7.0 , 9.22 , 2.83 , 7.28 , 10.3 , 1.41 , 9.9 , 0.0 , 10.2 , 0],
[ 0 , 11.4 , 12.08 , 14.21 , 3.61 , 4.12 , 8.94 , 3.0 , 12.08 , 11.05 , 9.49 , 10.2 , 0.0 , 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]];

float time_window_a[I]= [0, 67.55, 79.78, 84.54, 51.31, 45.26, 42.43, 62.6, 82.78, 36.83, 55.61, 54.0, 56.45, 60] ;

float time_window_b[I]= [160, 76.415, 93.514, 94.602, 61.003, 57.338, 49.459, 71.78, 96.514, 40.079, 68.993, 58.5, 68.285, 160.0] ;

//==================================================
dvar boolean x[I][I][K];
dvar float+ w[I][K];

dexpr float all_dist = sum(i,j in I,k in K)x[i][j][k]*distance[i][j];
minimize all_dist;
subject to
{
//	sum(i in J,k in K)x[i][0][k]==0;

  forall(i in 1..tot)// i==j must equal to 0
    sum(k in K)x[i][i][k]==0;

  forall(i in 1..tot)//cannot go back to 0
    sum(k in K)x[i][0][k]==0;

  forall(i in 1..tot)//cannot start from 11
    sum(k in K)x[tot+1][i][k]==0;

   forall(j in 1..tot)//every passenger must get drived only once
    sum(k in K,i in I)x[i][j][k]==1;

  forall(k in K)//must start from the airport
    sum(j in 1..tot+1)x[0][j][k]==1;

  forall(k in K)//must go to the final point
    sum(i in 0..tot)x[i][tot+1][k]==1;

  forall(k in K,j in 1..tot)//j is the central point//one car go in ,one car go out
      //sum(i in 0..tot:arrive_time[i]-arrive_time[j]<=30&&arrive_time[j]-arrive_time[i]<=30,m in 1..tot+1:arrive_time[i]-arrive_time[m]<30&&arrive_time[m]-arrive_time[i]<30)(x[i][j][k]-x[j][m][k])==0;
      sum(i in 0..tot,m in 1..tot+1)(x[i][j][k]-x[j][m][k])==0;

  forall(k in K,j in 1..tot)//the points that time  gap is too large
      sum(i in 1..tot:arrive_time[i]-arrive_time[j]>30||arrive_time[j]-arrive_time[i]>30)x[i][j][k]==0;

  forall(k in K)//every car can most drive 4 passenger
    sum(i in 0..tot+1,j in 1..tot+1)x[i][j][k]<=5;


  forall(k in K,i,j in 1..tot)//calculate the start time from airpoint
    w[0][k]>=x[i][j][k]*arrive_time[i];

  forall(k in K,i in 0..tot,j in 1..tot+1)
    w[i][k]+distance[i][j]*3-w[j][k]<=1000*(1-x[i][j][k]);

  forall(k in K ,i in 1..tot){
    sum(j in 1..tot+1)x[i][j][k]*time_window_a[i]<=w[i][k];
  	sum(j in 1..tot+1)x[i][j][k]*(time_window_b[i]+30)>=w[i][k];
  }
}

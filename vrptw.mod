/*********************************************
 * OPL 12.6.3.0 Model
 * Author: hedge
 * Creation Date: 2018-4-26 at 上午9:19:22
 *********************************************/
int tot=10;
range I=0..tot+1;//I is the terminal
range K=1..5;//K is the driver

//====================================================================

float arrive_time[I]= ...;

float distance[0..tot+1][0..tot+1]=...;

float time_window_a[I]= ... ;

float time_window_b[I]= ...;

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

  forall(k in K,i in 0..tot,j in 1..tot+1)//w[i][k]means the time when vihecle arrive point I
    w[i][k]+distance[i][j]*3-w[j][k]<=1000*(1-x[i][j][k]);

  forall(k in K ,i in 1..tot){  //time window
    sum(j in 1..tot+1)x[i][j][k]*time_window_a[i]<=w[i][k];
  	sum(j in 1..tot+1)x[i][j][k]*(time_window_b[i]+30)>=w[i][k];
  }
}

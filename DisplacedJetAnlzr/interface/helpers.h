#ifndef DJ_HELPERS
#define DJ_HELPERS

#include <numeric>
#include <math.h>

class helpers {
  public:

  float Avg (std::vector<float> data){
    if (data.empty()) return -1;
    return std::accumulate(data.begin(),data.end(),0.)/((float) data.size());
  }

  float AvgDistance(std::vector<float> data, float center){
    if (data.empty()) return -1;
    for(size_t i=0;i<data.size();i++){ data[i] = fabs(data[i]-center)/center; }
    return std::accumulate(data.begin(),data.end(),0.)/((float) data.size());
  }

  float RMS(std::vector<float> data, float center){
    if (data.empty()) return -1;
    for(size_t i=0;i<data.size();i++){ data[i] = (data[i]-center)/center; }
    return sqrt( std::inner_product(data.begin(),data.end(),data.begin(),0.)/((float) data.size()) );
  }

  std::vector<std::vector<float> > clusters(std::vector<float> data, float limit){
    std::sort(data.begin(),data.end(),cmp);
    std::vector<std::vector<float> > clusters;
    for(size_t i=0;i<data.size();i++){
      std::vector<float> single(1,data[i]);
      clusters.push_back(single);
    }
    Join(clusters,limit);  
    return clusters;
  }

  float Nclusters(std::vector<std::vector<float> > clusters){
    int N=0;
    for(size_t i=0;i<clusters.size();i++){
      if (clusters[i].size() > 1) N+=1;
    }
    return N;
  }

  std::vector<float> bestcluster(std::vector<std::vector<float> > clusters, float target){
    float min = 1e10;
    std::vector<float> bestcluster;
    if (clusters.size()==0) return bestcluster;
    for (size_t i=0;i<clusters.size();i++){
      if (clusters[i].size()<2) continue;
      float dist =  AvgDistance(clusters[i],target);
      if(dist < min){
        min = dist;
        bestcluster = clusters[i];
      }
    }
    return bestcluster;
  } 

  void printvec(std::vector<float> vec){
    for (size_t i=0;i<vec.size();i++) std::cout << vec[i] << " ";
    std::cout << std::endl;
  }

  void printvecvec(std::vector<std::vector<float> > vecvec){

    for (size_t i=0;i<vecvec.size();i++){
      std::vector<float> vec = vecvec[i];
      printvec(vec);
    }
  }

  private:

  float Linkage(std::vector<float> A, std::vector<float> B){
     float max=0;
     for (size_t i=0;i<A.size();i++)
       for (size_t j=0;j<B.size();j++){
         float dist = fabs(A[i]-B[j]);
         if (dist > max) max = dist;
       }
     return max;
  }

  void Join(std::vector<std::vector<float> > &obs, float limit){

    float min=1e10;
    std::pair<int,int> toJoin;
    for (int i=0; i<int(obs.size()-1); i++){
      for(size_t j=i+1; j<obs.size();j++){
        std::vector<float> obs1 = obs[i];
        std::vector<float> obs2 = obs[j];
        float distance = Linkage(obs1,obs2);
        if (distance<min){
          toJoin = std::pair<int,int>(i,j);
          min = distance;
        } 
      }
    } 
    if (min < limit){
      std::vector<float> new_obs = obs[toJoin.first];
      new_obs.insert(new_obs.end(),obs[toJoin.second].begin(),obs[toJoin.second].end());
      // this is dumb removal of 2 objects, but I don't want to deal with it
      if (toJoin.first < toJoin.second){
        obs.erase(obs.begin()+toJoin.first);
        obs.erase(obs.begin()+toJoin.second - 1);
      } else {
        obs.erase(obs.begin()+toJoin.first);
        obs.erase(obs.begin()+toJoin.second);
      } 

      obs.push_back(new_obs);
      Join(obs,limit);
    } else {
      return;
    }
  }

  static bool cmp(float a, float b) {return (a<b);}
};

#endif

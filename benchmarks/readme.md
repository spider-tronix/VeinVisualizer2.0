## Benchmarks:
This folder contains all the benchmarking scripts and parameters. The task is to have a systematic study and comparision of timing response, frame rates, image sizes etc. 
    
## TODO:
-  [x] Add benchmarking video/dataset for comparison
-  [x] Combine individual scripts into a single file
-  [ ] Compare video vs camera read performance
-  [x] Compare system performance vs rasperry pi performance
-  [ ] Explore options for optimizing the code.

| Device            | Frames per Second |OpenCV optimization|
| ----------------- | ----------------- | ----------------- |
| i3-4005U 1.7GHz   | 31.87             |        No         |
| Raspberry Pi 3B+  | 9.37              |        No         |
| Raspberry Pi 3B+  | 14.48             |        Yes        | 
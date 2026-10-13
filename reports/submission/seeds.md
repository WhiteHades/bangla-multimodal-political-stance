| Population | Model | Seeds | Mean macro-F1 | SD | Min | Max |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| all_headlines | bangla_electra | 5 | 0.370 | 0.024 | 0.328 | 0.386 |
| all_headlines | banglabert | 5 | 0.454 | 0.033 | 0.413 | 0.496 |
| all_headlines | majority | 5 | 0.228 | 0.000 | 0.228 | 0.228 |
| all_headlines | mbert | 5 | 0.454 | 0.026 | 0.430 | 0.490 |
| all_headlines | mt5 | 5 | 0.342 | 0.059 | 0.282 | 0.439 |
| all_headlines | tfidf_logreg | 5 | 0.501 | 0.011 | 0.491 | 0.517 |
| all_headlines | xlmr | 5 | 0.339 | 0.028 | 0.320 | 0.387 |
| paired_headlines | align | 5 | 0.316 | 0.063 | 0.253 | 0.406 |
| paired_headlines | bangla_electra | 5 | 0.336 | 0.022 | 0.308 | 0.365 |
| paired_headlines | banglabert | 5 | 0.402 | 0.062 | 0.328 | 0.473 |
| paired_headlines | blip | 5 | 0.322 | 0.037 | 0.263 | 0.356 |
| paired_headlines | clip | 5 | 0.370 | 0.040 | 0.307 | 0.410 |
| paired_headlines | countvec_vit | 5 | 0.370 | 0.034 | 0.335 | 0.421 |
| paired_headlines | flava | 5 | 0.285 | 0.037 | 0.231 | 0.319 |
| paired_headlines | majority | 5 | 0.208 | 0.000 | 0.208 | 0.208 |
| paired_headlines | mbert | 5 | 0.398 | 0.027 | 0.374 | 0.443 |
| paired_headlines | mt5 | 5 | 0.357 | 0.050 | 0.285 | 0.407 |
| paired_headlines | tfidf_logreg | 5 | 0.562 | 0.046 | 0.512 | 0.611 |
| paired_headlines | vilt | 5 | 0.308 | 0.053 | 0.230 | 0.378 |
| paired_headlines | xlmr | 5 | 0.313 | 0.023 | 0.277 | 0.338 |

| VL model | Reference | Seeds | Mean Δ | SD | Min | Max | CI>0 | CI<0 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| align | banglabert | 5 | -0.086 | 0.094 | -0.173 | +0.055 | 0 | 2 |
| align | tfidf_logreg | 5 | -0.246 | 0.077 | -0.321 | -0.117 | 0 | 4 |
| blip | banglabert | 5 | -0.080 | 0.047 | -0.125 | -0.010 | 0 | 0 |
| blip | tfidf_logreg | 5 | -0.240 | 0.048 | -0.293 | -0.164 | 0 | 5 |
| clip | banglabert | 5 | -0.032 | 0.055 | -0.064 | +0.065 | 0 | 0 |
| clip | tfidf_logreg | 5 | -0.192 | 0.027 | -0.217 | -0.157 | 0 | 4 |
| countvec_vit | banglabert | 5 | -0.032 | 0.042 | -0.102 | +0.007 | 0 | 0 |
| countvec_vit | tfidf_logreg | 5 | -0.192 | 0.064 | -0.276 | -0.130 | 0 | 3 |
| flava | banglabert | 5 | -0.117 | 0.051 | -0.159 | -0.028 | 0 | 3 |
| flava | tfidf_logreg | 5 | -0.277 | 0.032 | -0.311 | -0.236 | 0 | 5 |
| vilt | banglabert | 5 | -0.094 | 0.100 | -0.243 | -0.019 | 0 | 1 |
| vilt | tfidf_logreg | 5 | -0.254 | 0.094 | -0.379 | -0.135 | 0 | 4 |

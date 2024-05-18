install.packages("tidyverse")
library(tidyverse)

dados <- readr::read_csv("/home/espinf/dafpereira/Downloads/Mental Health Dataset.csv")
glimpse(dados)
library(dplyr)
library(forcats)
library(lubridate)
library(readr)
library(tibble)
library(tidyr)
library(magrittr)
library(data.table)


glimpse(dados)


dados <- dados %>%
  mutate(mercosul = ifelse(Country %in%
             c("Argentina", "Brazil", "Paraguay", "Uruguay"),
             "Mercosul", "Não Mercosul"))
glimpse(dados)

dados2 <- dados %>%
  select(Country, Timestamp, Days_Indoors, mercosul)
glimpse(dados2)

car_crash <- fread("/home/espinf/dafpereira/Downloads/Brazil Total highway crashes 2010 - 2023.csv.gz")
glimpse(car_crash)

car_crash2 <- car_crash %>%
  filter (tipo_de_ocorrencia == "sem vítima" & automovel >= 3)
glimpse(car_crash2)  




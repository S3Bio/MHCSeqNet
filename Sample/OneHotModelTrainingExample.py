import pandas as pd

from MHCSeqNet.PredictionModel.BindingOnehotPredictor import BindingOnehotPredictor

allele_to_train = ["HLA-A*01:01","HLA-A*02:01","HLA-A*02:02","HLA-A*02:03","HLA-A*02:04","HLA-A*02:05","HLA-A*02:06",
                   "HLA-A*02:07","HLA-A*02:11","HLA-A*02:17","HLA-A*03:01","HLA-A*11:01","HLA-A*23:01","HLA-A*24:02",
                   "HLA-A*24:03","HLA-A*24:06","HLA-A*24:13","HLA-A*25:01","HLA-A*26:01","HLA-A*26:02","HLA-A*29:02",
                   "HLA-A*30:01","HLA-A*30:02","HLA-A*31:01","HLA-A*32:01","HLA-A*33:01","HLA-A*66:01","HLA-A*68:01",
                   "HLA-A*68:02","HLA-A*69:01","HLA-A*80:01","HLA-B*07:02","HLA-B*08:01","HLA-B*08:02","HLA-B*13:01",
                   "HLA-B*13:02","HLA-B*14:02","HLA-B*15:01","HLA-B*15:02","HLA-B*15:09","HLA-B*15:11","HLA-B*15:17",
                   "HLA-B*18:01","HLA-B*18:03","HLA-B*27:01","HLA-B*27:02","HLA-B*27:03","HLA-B*27:04","HLA-B*27:05",
                   "HLA-B*27:06","HLA-B*27:07","HLA-B*27:09","HLA-B*35:01","HLA-B*35:03","HLA-B*35:08","HLA-B*38:01",
                   "HLA-B*39:01","HLA-B*39:24","HLA-B*40:01","HLA-B*40:02","HLA-B*41:01","HLA-B*41:03","HLA-B*41:04",
                   "HLA-B*44:02","HLA-B*44:03","HLA-B*44:08","HLA-B*44:27","HLA-B*44:28","HLA-B*45:01","HLA-B*46:01",
                   "HLA-B*48:01","HLA-B*49:01","HLA-B*50:01","HLA-B*51:01","HLA-B*51:08","HLA-B*53:01","HLA-B*54:01",
                   "HLA-B*56:01","HLA-B*57:01","HLA-B*58:01","HLA-C*01:02","HLA-C*03:03","HLA-C*03:04","HLA-C*04:01",
                   "HLA-C*05:01","HLA-C*06:02","HLA-C*07:01","HLA-C*07:02","HLA-C*08:01","HLA-C*08:02","HLA-C*15:02",
                   "HLA-C*16:01"]

df = pd.read_csv('MHCSeqNet/PredictionModel/Data/mhc_ligand_NP_20171025_cleaned.csv')
df = df[df.allele.isin(allele_to_train)]

df = df.replace(to_replace='Positive', value=1.0)
df = df.replace(to_replace='Positive-High', value=1.0)
df = df.replace(to_replace='Negative', value=0.0)

bindingOnehotPredictor = BindingOnehotPredictor()
bindingOnehotPredictor.train_model('Models/one_hot_model_example/',
                                   df.peptide.values,
                                   df.allele.values,
                                   df.binding_quality.values,
                                   amino_acid_representation_path="MHCSeqNet/AminoAcidRepresentationModel/Model/embedding_weight_merged_5_d6.h5")

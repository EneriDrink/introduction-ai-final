# 🌱 Project Title 
![nccuintellibox](https://github.com/EneriDrink/introduction-ai-final/assets/114038939/deb3fcd7-fc0a-4ec3-8c42-bce90907211f)

## 🌷 Project Description

Every day, international students in National Chengchi University receive a significant number of school emails regarding various school events. However, due to the emails being written in Chinese and the sheer volume of messages received, the task of individually opening, translating, and deciding which events to participate in becomes incredibly time-consuming. Consequently, many international students refrain from opening these emails altogether, inadvertently missing out on numerous interesting and important school events.

Which is why the primary objective of this project is to develop an ***artificial intelligence (AI) powered email translator*** specifically tailored for international students. The proposed AI system will ***efficiently translate Chinese emails into English, thereby removing language barriers and ensuring equal access to academic information and resources for all students.*** This school email translator AI will serve as a vital tool, enabling international students to comprehend crucial details such as assignments, campus events, administrative updates, and dormitory information.

## 🫧 Getting Started

**Steps**

- make sure python is installed
- make new virtual env:
```bash
python3 -m venv ./venv 
```

- activate virtual env
```bash
source venv/bin/activate  
```

- install requirements:

```bash
pip install requirements.txt
```

- run the script( it takes more or less 16 minutes):

```
python main.py
```


## 🪐 File Structure

+ Preprocessed Dataset (google sheets)
+ Open AI  code
+ Hugging Face code
+ Google translate code
+ outputs

## 🌼 Analysis

Our result comparison table
| Tools              | Title        | Message  |
| -------------      | ------------ | -------- |
| `Original Message` | 自強服務中心通知 | 同學，您好： 2/23(四) 10:00-17:00將進行自九舍洗衣機更換，期間請勿使用洗衣機，造成不便敬請見諒，謝謝。|
| `Open AI`          | Notification from Zi Chiang  Service Center | Hello students, On February 23rd (Thursday) from 10:00 to 17:00, we will be replacing the washing machines in the 9th dormitory. During this period, please do not use the washing machines. We apologize for any inconvenience this may cause and thank you for your cooperation. Best regards. |
| `Hugging Face`  | Notification by the Forced Center | You are good: 2/23 (iv) 1017:00 stereotypes are more developed from nine swashings, do not use washings, causing unrelenting of the indicators, etc. |
| `Google Translate` | Self-improvement service center notice | Hello, classmates: 2/23 (Thursday) 10:00-17:00 will replace the washing machine from Jiushe. Please do not use the washing machine during this period. Sorry for the inconvenience, thank you. |

## ✨ Results

In conclusion, the evaluation of translation models for Chinese-to-English email translation clearly demonstrates that OpenAI outperforms Hugging Face in terms of reliability and accuracy. OpenAI consistently provides accurate and contextually appropriate translations, ensuring international students receive clear and comprehensible information. In contrast, Hugging Face and Goggle's literal translation approach often leads to confusing and nonsensical translations, limiting its reliability as an effective email translation solution. The advanced language models and extensive training of OpenAI contribute to its superior performance, enabling international students to overcome language barriers and actively engage with academic resources. Therefore, ***OpenAI*** is recommended as the preferred choice for the proposed email translation solution, ensuring reliable and accessible translations for international students.

| APIs | Summary |
| --------- | -------------- |
| ![ChatGPT](https://img.shields.io/badge/chatGPT-74aa9c?style=for-the-badge&logo=openai&logoColor=white) | Most Accurate, Able to understand the context and make the approprite translation |
| ![Google Translate](https://img.shields.io/badge/google%20translate-4285F4?style=for-the-badge&logo=google%20translate&logoColor=white) | Able to translate every word but lacks understanding of the context |
| ![Huggingface🤗](https://img.shields.io/badge/🤗Hugging%20Face-%23f2f2f2.svg?style=for-the-badge&logo=hugging%20face&logoColor=white) | Is **not** reliable enough to produce the correct translation in any situation. However, it performs a bit better when there is english word intergrated into the emails |

## 🍀 Contributors

group AI-07
|Student ID |  Roles & Contributions |
| --------- | ---------------------- |
|`109ZU1014  創國三   陳鴻彬`| project manager, reasearch, project presentation |
|`111ZU1033  創國一   黃  莉`| coding, research, debugging, Making sure everyone does their job and helps, poster, ppt |
|`111703029  資科一   劉  白`| coding, research, debugging, github README file |
|`111703034  資科一   張佳佳`| coding, data preprocessing, poster |
|`111ZU1018  創國一   許瑈芸`| Data collection and ensure the dataset's quailty | ]

## 🍄 Acknowledgments

We would like to express our sincere gratitude to the following team members for their contributions (as shown above) to the development of our NCCU Intellibox, Chinese-to-English email translation AI:

+ 陳鴻彬
+ 黃   莉
+ 劉  白
+ 張佳佳
+ 許瑈芸

We would also like to extend our sincere appreciation to our instructor, Professor  **Chung-pei Pien (卞中佩)**, for their guidance, expertise, and unwavering support throughout this project.

## 🌙 References

GOOGLE COLAB LINKS

`open ai` https://colab.research.google.com/drive/15n6P1RblyzHqIiIWi0P_W2jqC52-DmC4?usp=sharing

`OpenAI and Google Translate, manually translated` https://colab.research.google.com/drive/1migTqAddNFUWzm6cEjsWJRgSwoycNdyz?usp=sharing 

`Hugging Face model` https://colab.research.google.com/drive/1Ci63rcMOwJIP1mWTnWP-i4bS-ZfjzKbm?usp=sharing 


`Information about our AI` https://www.canva.com/design/DAFl0eAvEoQ/CjOGlJKFs8jvLfBjKXlFrw/view?utm_content=DAFl0eAvEoQ&utm_campaign=designshare&utm_medium=link&utm_source=viewer

`Translation Results` https://docs.google.com/spreadsheets/d/1CiDBNIqVxQqycSCenYy0p3_rOnDrDetDBDeGWaH_Zn4/edit?usp=sharing 

 

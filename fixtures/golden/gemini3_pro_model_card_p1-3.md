# Gemini 3 Pro Model Card

## Gemini 3 Pro - Model Card

**Model Cards** are intended to provide essential information on Gemini models, including known limitations, mitigation approaches, and safety performance. Model cards may be updated from time-to-time; for example, to include updated evaluations as the model is improved or revised. See the Google DeepMind site for a comprehensive list of model cards.

This model card includes more essential information about the Gemini 3 family of models than previous model cards did. We hope more information about the training dataset, distribution, and intended uses will empower developers with deeper insights and help build more robust and responsible downstream applications.

*Model Release: November 2025*

## Model Information

**Description:** Gemini 3 Pro is the next generation in the Gemini series, a suite of highly-capable, natively multimodal, reasoning models. Gemini 3 Pro is now Google's most advanced model for complex tasks, and can comprehend vast datasets and challenging problems from different information sources, including text, audio, images, video, and entire code repositories. Gemini 3 Pro now features Deep Think mode, an optional setting designed to enhance complex problem-solving performance at time of inference.

**Model dependencies:** This model is not a modification or a fine-tune of a prior model.

**Inputs:** Text strings (e.g., a question, a prompt, document(s) to be summarized), images, audio, and video files, with a token context window of up to 1M.

**Outputs:** Text, with a 64K token output.

**Architecture:** Gemini 3 Pro is a sparse mixture-of-experts (MoE) (Clark et al., 2022; Du et al., 2021; Fedus et al., 2021; Jiang et al., 2024, Lepikhin et al., 2020; Riquelme et al., 2021; Roller et al., 2021; Shazeer et al., 2017) transformer-based model (Vaswani et al., 2017) with native multimodal support for text, vision, and audio inputs. Sparse MoE models activate a subset of model parameters per input token by learning to dynamically route tokens to a subset of parameters (experts); this allows them to decouple total model capacity from computation and serving cost per token. Developments to the model architecture contribute to the significantly improved performance from previous model families.

## Model Data

**Training Dataset:** The pre-training dataset was a large-scale, diverse collection of data encompassing a wide range of domains and modalities, which included publicly-available web-documents, text, code, images, audio (including speech and other audio types) and video. The post-training dataset included different types of instruction tuning data, reinforcement learning data, and human-preference data. Gemini 3 Pro is trained using reinforcement learning techniques that can leverage multi-step reasoning, problem-solving and theorem-proving data.

The training dataset also includes: publicly available datasets that are readily downloadable; data obtained by crawlers; licensed data obtained via commercial licensing agreements; user data (i.e., data collected from users of Google products and services to train AI models, along with user interactions with the model) in accordance with Google's relevant terms of service, privacy policy, service-specific policies, and pursuant to user controls, where appropriate; other datasets that Google acquires or generates in the course of its business operations, or directly from its workforce; and AI-generated synthetic data.

**Training Data Processing:** Data filtering and preprocessing included techniques such as deduplication, honoring robots.txt, safety filtering in-line with Google's commitment to advancing AI safely and responsibly, and quality filtering to mitigate risks and improve training data reliability. Once data is collected, it is cleaned and preprocessed to make it suitable for training. This process involves, on a case-by-case basis, filtering irrelevant or harmful content, text, and other modalities, including filtering content that is pornographic, violent, or violative of child sexual abuse material (CSAM) laws.

## Implementation and Sustainability

**Hardware:** Gemini 3 Pro was trained using Google's Tensor Processing Units (TPUs). TPUs are specifically designed to handle the massive computations involved in training LLMs and can speed up training considerably compared to CPUs. TPUs often come with large amounts of high-bandwidth memory, allowing for the handling of large models and batch sizes during training, which can lead to better model quality. TPU Pods (large clusters of TPUs) also provide a scalable solution for handling the growing complexity of large foundation models. Training can be distributed across multiple TPU devices for faster and more efficient processing.

The efficiencies gained through the use of TPUs are aligned with Google's commitment to operate sustainably.

**Software:** Training was done using JAX and ML Pathways.

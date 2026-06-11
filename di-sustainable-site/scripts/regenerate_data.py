#!/usr/bin/env python3
"""
Regenerate data.js from a Python data structure using json.dumps.
This ensures all quotes, unicode, and special characters are properly escaped.
"""

import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
DATA_JS = os.path.join(PROJECT_DIR, "data.js")

# Build the complete faculty data as Python dicts
# This avoids all quote/encoding issues

data = [
  {
    "id": "francesca-valsecchi",
    "photo": "images/photo-francesca-valsecchi.webp",
    "name_zh": "\u9b4f\u4f5b\u5170",
    "name_en": "Francesca Valsecchi",
    "title_zh": "\u526f\u6559\u6388",
    "title_en": "Associate Professor",
    "bio_zh": "\u9b4f\u4f5b\u5170\u535a\u58eb\uff0c\u73b0\u4efb\u540c\u6d4e\u5927\u5b66\u8bbe\u8ba1\u521b\u610f\u5b66\u9662\u526f\u6559\u6388\u3002\u4ece\u53c2\u4e0e\u5f0f\u8bbe\u8ba1\u7814\u7a76\u5230\u6c89\u6d78\u5f0f\u827a\u672f\u5b9e\u8df5\uff0c\u9b4f\u4f5b\u5170\u526f\u6559\u6388\u7684\u5de5\u4f5c\u81f4\u529b\u4e8e\u63a2\u7d22\u201c\u7eff\u8272\u611f\u77e5\uff08green sense\uff09\u201d\u4f5c\u4e3a\u4eba\u7c7b\u611f\u77e5\u4e0e\u8ba4\u77e5\u4e0b\u4e00\u79cd\u4e34\u754c\u7a7a\u95f4\u7684\u53d1\u5c55\u65b9\u5411\u3002\u5979\u73b0\u4e8e\u4e0a\u6d77\u540c\u6d4e\u5927\u5b66\u8bbe\u8ba1\u521b\u610f\u5b66\u9662\u5f00\u5c55\u6559\u5b66\u4e0e\u7814\u7a76\u5de5\u4f5c\uff0c\u5e76\u521b\u7acb\u4e86\u201c\u751f\u6001\u4e0e\u6587\u5316\u521b\u65b0\u5b9e\u9a8c\u5ba4\uff08Ecology and Cultures Innovation Lab\uff09\u201d\uff0c\u4ee5\u8ba8\u8bba\u548c\u5b9e\u9a8c\u201c\u8d85\u8d8a\u4eba\u7c7b\u4e2d\u5fc3\uff08more-than-human\uff09\u201d\u7684\u8bbe\u8ba1\u65b9\u6cd5\uff0c\u4ee5\u53ca\u540e\u53d1\u5c55\uff08post-development\uff09\u8303\u5f0f\u6240\u9762\u4e34\u7684\u6311\u6218\u3002\u5979\u7684\u7814\u7a76\u6db5\u76d6\u5df2\u53d1\u8868\u7814\u7a76\u3001\u601d\u8fa8\u8bbe\u8ba1\u53ca\u5c55\u89c8\u5b9e\u8df5\uff0c\u4e3b\u9898\u5305\u62ec\u751f\u6001\u7cfb\u7edf\u5236\u56fe\u3001\u6c34\u57df\u666f\u89c2\u6c11\u65cf\u5fd7\u3001\u751f\u6001\u6570\u636e\u3001\u57ce\u5e02\u4e0e\u81ea\u7136\u4e92\u52a8\uff0c\u4ee5\u53ca\u793e\u4f1a\u8bbe\u8ba1\u7b49\u3002\u5979\u6765\u81ea\u610f\u5927\u5229\uff0c\u4f46\u5df2\u5728\u4e9a\u6d32\u751f\u6d3b\u548c\u5de5\u4f5c\u8d85\u8fc7\u5341\u5e74\u3002\u5979\u7684\u6559\u5b66\u4e0e\u7814\u7a76\u9879\u76ee\u6d89\u53ca\u201c\u8bbe\u8ba1\u4e0e\u81ea\u7136\u201d\u201c\u57ce\u4e61\u521b\u65b0\u201d\u201c\u53ef\u6301\u7eed\u98df\u7269\u7cfb\u7edf\u201d\uff0c\u4ee5\u53ca\u8fd1\u5e74\u6765\u8fdb\u4e00\u6b65\u62d3\u5c55\u7684\u201c\u751f\u6001\u7cfb\u7edf\u8bbe\u8ba1\uff08Design for Ecosystems\uff09\u201d\u65b9\u5411\u3002\u5979\u5728\u521b\u9020\u529b\u65b9\u6cd5\u3001\u53ef\u89c6\u5316\u65b9\u6cd5\u4ee5\u53ca\u53c2\u4e0e\u5f0f\u6280\u672f\u65b9\u9762\u5177\u6709\u4e30\u5bcc\u7ecf\u9a8c\uff0c\u5e76\u5e7f\u6cdb\u5e94\u7528\u4e8e\u6d89\u53ca\u516c\u4f17\u4e0e\u793e\u533a\u7684\u827a\u672f\u53ca\u7814\u7a76\u9879\u76ee\u4e2d\u3002\u540c\u65f6\uff0c\u5979\u6301\u7eed\u8fdb\u884c\u4ee5\u66ff\u4ee3\u6444\u5f71\u5de5\u827a\u4e0e\u751f\u7269\u5a92\u4ecb\u4e3a\u6838\u5fc3\u7684\u827a\u672f\u5b9e\u8df5\uff0c\u5e76\u79ef\u6781\u53c2\u4e0e\u73af\u5883\u884c\u52a8\u4e3b\u4e49\u3002",
    "bio_en": "From participatory design research to immersive artistic practice, the work of Associate Professor Francesca Valsecchi looks at developing the \"green sense\" as the next liminal space of human perception and cognition. She works in Shanghai at Tongji University, College of Design and Innovation. She established the Ecology and Cultures Innovation Lab to discuss and experiment on more-than-human design and the challenges of post-development paradigms. Her research includes published, speculative and exhibition works about mapping ecosystems, ethnography of waterscapes, ecological data, and urban-nature interaction, and social design. She is Italian, but she has been in Asia for more than a decade. Her teaching and research projects cover the areas of Design and Nature, Rural-Urban Innovation, Sustainable Food Systems, and more recently in the direction of Design for Ecosystems. She is an expert in creativity and visualization methods and participatory techniques, which she applied largely in artistic and research projects involving citizens and communities. She has an ongoing artistic practice using alternative photographic processes and bio-media. She is an environmental activist.",
    "tags": ["Systemic Design", "Participatory Design", "Ecology", "More-than-Human"],
    "achievements": [
      {
        "name_zh": "\u6d77\u5cb8\u8bd7\u5b66\uff1a\u6d77\u5cb8\u5171\u521b\u827a\u672f\u9a7b\u7559\u8ba1\u5212",
        "name_en": "Poetry of the Coasts: Coastal Co-Art Residency",
        "description_zh": "\u6d77\u5cb8\u751f\u6001\u7cfb\u7edf\u662f\u7531\u6f6e\u6c50\u3001\u6ce5\u6c99\u6d41\u52a8\u3001\u76d0\u5ea6\u68af\u5ea6\u3001\u8fc1\u5f99\u7269\u79cd\u4ee5\u53ca\u4eba\u7c7b\u9002\u5e94\u884c\u4e3a\u5171\u540c\u5851\u9020\u7684\u52a8\u6001\u7cfb\u7edf\u3002\u201c\u6d77\u5cb8\u8bd7\u5b66\u201d\u662f\u4e00\u9879\u4e3a\u671f\u4e00\u5e74\u7684\u9879\u76ee\uff0c\u7531\u82f1\u56fd\u6587\u5316\u534f\u4f1a\u8d44\u52a9\uff0c\u5e76\u5f97\u5230\u540c\u6d4e\u5927\u5b66\u4e0e\u5170\u5361\u65af\u7279\u5927\u5b66\u652f\u6301\u3002\u9879\u76ee\u901a\u8fc7\u5728\u4e2d\u56fd\u5d07\u660e\u5c9b\u4e0e\u82f1\u56fd\u83ab\u514b\u59c6\u6e7e\u5f00\u5c55\u76f8\u4e92\u5173\u8054\u7684\u827a\u672f\u5bb6\u9a7b\u7559\uff0c\u53d1\u5c55\u4e00\u7cfb\u5217\u4f7f\u8de8\u5c3a\u5ea6\u7ea0\u7f20\u5173\u7cfb\u53ef\u89c6\u5316\u7684\u521b\u4f5c\u5b9e\u8df5\u3002\u8be5\u9879\u76ee\u7ed3\u5408\u751f\u6001\u827a\u672f\u3001\u53c2\u4e0e\u5f0f\u8bbe\u8ba1\u3001\u73af\u5883\u4eba\u6587\u5b66\u4ee5\u53ca\u7530\u91ce\u89c2\u5bdf\u7b49\u8de8\u5b66\u79d1\u65b9\u6cd5\uff0c\u5728\u82f1\u56fd\u4e0e\u4e2d\u56fd\u4e4b\u95f4\u751f\u6210\u65b0\u7684\u8de8\u6587\u5316\u751f\u6001\u5b66\u4e60\u6a21\u5f0f\u3002",
        "description_en": "The Poetry of the Coasts is a year-long project funded by the British Council and supported by Tongji and Lancaster University. It develops intertwined artists' residencies in the coastal environments of Chongming Island (China) and Morecambe Bay (UK). The project combines transdisciplinary methods from ecological art, participatory design, environmental humanities, and field-based observation, generating new forms of intercultural ecological learning between the UK and China."
      },
      {
        "name_zh": "\u9ec4\u9f99\u58f0\u666f\u751f\u6001\u6b65\u9053",
        "name_en": "Huanglong Acoustic Ecology Interpretation Trail",
        "description_zh": "\u4e0eCAUP\uff08\u5efa\u7b51\u4e0e\u57ce\u5e02\u89c4\u5212\u5b66\u9662\uff09\u5408\u4f5c\uff0c\u5728\u56db\u5ddd\u9ec4\u9f99\u516c\u56ed\uff08UNESCO\u4e16\u754c\u9057\u4ea7\uff09\u5efa\u8bbe\u58f0\u666f\u751f\u6001\u89e3\u8bf4\u6b65\u9053\u3002\u9879\u76ee\u65e8\u5728\u89e3\u51b3\u4f20\u7edf\u81ea\u7136\u5c55\u89c8\u4e2d\u751f\u7269\u591a\u6837\u6027\u201c\u770b\u4e0d\u89c1\u3001\u542c\u4e0d\u5230\u201d\u7684\u5173\u952e\u5c40\u9650\uff0c\u5c06\u58f0\u666f\u4e0e\u6b65\u9053\u8bbe\u8ba1\u76f8\u7ed3\u5408\u3002",
        "description_en": "In collaboration with CAUP (College of Architecture and Urban Planning), the Huanglong Acoustic Ecology Interpretation Trail addresses a key limitation of conventional nature exhibition: biodiversity is largely invisible and inaudible. Located in Huanglong Park, a UNESCO World Heritage site in Sichuan, China, the trail integrates soundscape interpretation into the walking experience."
      }
    ],
    "courses": [
      {
        "name_zh": "Studio 1\u2014\u2014\u751f\u6001\u590d\u6742\u6027\u53d9\u4e8b\u7684\u4f20\u64ad\u4e0e\u5a92\u4ecb\u5de5\u5177",
        "name_en": "Studio 1 \u2014 Communication and Media Tools for the Narrative of Ecological Complexity (MA)",
        "description_zh": "\u4e0a\u6d77\u662f\u4e00\u5ea7\u7531\u6c34\u5851\u9020\u7684\u8d85\u7ea7\u57ce\u5e02\uff0c\u4f46\u5176\u5e7f\u9614\u7684\u6d77\u5cb8\u8fb9\u7f18\u5730\u5e26\u5bf9\u5927\u591a\u6570\u5c45\u6c11\u800c\u8a00\u4ecd\u662f\u964c\u751f\u7a7a\u95f4\u3002\u672c\u5de5\u4f5c\u5ba4\u5c06\u6d77\u5cb8\u89c6\u4e3a\u4e0a\u6d77\u53d9\u4e8b\u4e2d\u7684\u6838\u5fc3\u89d2\u8272\uff0c\u901a\u8fc7\u8bbe\u8ba1\u7814\u7a76\u7ed8\u5236\u53ef\u89c1\u4e0e\u4e0d\u53ef\u89c1\u7684\u591a\u91cd\u5c42\u6b21\uff0c\u6784\u5efa\u201c\u6311\u8845\u6027\u63d0\u6848\u4e0e\u7814\u7a76\u7269\u4ef6\u201d\u8d44\u6599\u5e93\uff0c\u4f5c\u4e3a\u9a7b\u7559\u827a\u672f\u5bb6\u7684\u6838\u5fc3\u7814\u7a76\u7d20\u6750\u3002",
        "description_en": "Shanghai is a megacity defined by its relationship with water, yet its vast coastal edges remain largely unknown to its inhabitants. This studio interprets the coast as a central character in Shanghai's story. Students produce a rich repository of \"Provocations & Artefacts\" as primary research material for artists-in-residence."
      },
      {
        "name_zh": "\u6570\u636e\u53ef\u89c6\u5316\u2014\u2014\u57ce\u5e02\u751f\u6001\u7684\u6570\u636e\u7ed3\u6784\u4e0e\u53d9\u4e8b",
        "name_en": "Data Visualisation \u2014 Visual Structures & Data Stories of Urban Ecology (MA)",
        "description_zh": "\u805a\u7126\u6570\u636e\u53ef\u89c6\u5316\u7684\u5f3a\u5316\u6559\u5b66\u6a21\u5757\uff0c\u81ea2014\u5e74\u5f00\u8bbe\u30022026\u7248\u8bfe\u7a0b\u901a\u8fc7\u4eba\u5de5\u667a\u80fd\u589e\u5f3a\u5b9e\u8df5\u3001\u5de5\u5177\u57fa\u51c6\u6bd4\u8f83\u4ee5\u53ca\u6279\u5224\u6027\u89c6\u89c9\u5206\u6790\uff0c\u91cd\u65b0\u5b9a\u4e49\u6570\u636e\u53ef\u89c6\u5316\u9886\u57df\u3002\u53ef\u89c6\u5316\u540c\u65f6\u4f5c\u4e3a\u7814\u7a76\u65b9\u6cd5\u548c\u516c\u5171\u4f20\u64ad\u5a92\u4ecb\u3002",
        "description_en": "An intensive module in data visualisation launched in 2014. The 2026 edition experiments with AI-augmented practices, tool benchmarking, and critical visual analysis. Visualisation is addressed in its dual capacity: as a research methodology and as a public communication artefact."
      },
      {
        "name_zh": "Studio 5\u2014\u2014\u57ce\u5e02\u81ea\u7136",
        "name_en": "Studio 5 \u2014 Urban Nature (BA)",
        "description_zh": "\u8bbe\u8ba1\u80fd\u591f\u63d0\u5347\u57ce\u5e02\u5c45\u6c11\u751f\u6001\u7d20\u517b\u7684\u4eba\u5de5\u7269\uff0c\u4f7f\u5176\u4f5c\u4e3a\u57ce\u5e02\u751f\u6001\u666f\u89c2\u4e2d\u7684\u201c\u751f\u6001\u53ef\u4f9b\u6027\u201d\u53d1\u6325\u4f5c\u7528\u3002",
        "description_en": "Designing artefacts that support ecological literacy among city dwellers and function as ecological affordances in the urban ecology landscape."
      },
      {
        "name_zh": "Studio 5\u2014\u2014\u611f\u77e5\u751f\u6001",
        "name_en": "Studio 5 \u2014 Sensing Ecology (BA)",
        "description_zh": "\u4ee5\u751f\u6001\u4ee3\u8c22\u7cfb\u7edf\u4e2d\u7684\u8f93\u5165\u2014\u8f93\u51fa\u673a\u5236\u4e3a\u7075\u611f\uff0c\u5f00\u5c55PCB\u7535\u8def\u8bbe\u8ba1\u4e0e\u7f16\u7a0b\u57fa\u7840\u8bfe\u7a0b\u3002",
        "description_en": "Foundational course of PCB design and programming taking inspiration from input-output mechanism of ecological metabolic system."
      }
    ],
    "gallery": [
      {"src": "images/residence-artist-zhu-chen-at.webp", "caption_zh": "\u9a7b\u7559\u827a\u672f\u5bb6\u6731\u6668\u5728\u8fdb\u884c\u5173\u4e8e\u68ee\u6797\u4e0e\u9e1f\u7c7b\u7ea0\u7f20\u5173\u7cfb\u7684\u521b\u4f5c\u5b9e\u8df5", "caption_en": "Residence artist (Zhu Chen) at work with the forest/birds entanglement"},
      {"src": "images/tongji-students-in-a-fieldwork.webp", "caption_zh": "\u540c\u6d4e\u5927\u5b66\u5b66\u751f\u4e0e\u6d77\u6d0b\u5730\u8d28\u56fd\u5bb6\u91cd\u70b9\u5b9e\u9a8c\u5ba4\u5730\u8d28\u5b66\u5bb6\u5171\u540c\u5f00\u5c55\u4e34\u6e2f\u6d77\u5cb8\u751f\u6001\u7cfb\u7edf\u7530\u91ce\u8c03\u67e5", "caption_en": "Tongji students in a fieldwork with the geologist of Tongji Marine Geology Key Laboratory to study the coastal ecosystem in Lingang"},
      {"src": "images/residence-artists-exploration.webp", "caption_zh": "\u9a7b\u7559\u827a\u672f\u5bb6\u5bf9\u5d07\u660e\u5c9b\u8fd0\u6cb3\u7cfb\u7edf\u7684\u63a2\u7d22\u7814\u7a76", "caption_en": "Residence artists' exploration of Chongming Island canals"},
      {"src": "images/sample-of-the-birdscape-explor.webp", "caption_zh": "\u9e1f\u7c7b\u58f0\u666f\u63a2\u7d22\u4ea4\u4e92\u754c\u9762\u793a\u4f8b", "caption_en": "Sample of the birdscape exploration interface"},
      {"src": "images/photographs-of-the-constructed.webp", "caption_zh": "\u9ec4\u9f99\u516c\u56ed\u5df2\u5efa\u6210\u9e1f\u7c7b\u58f0\u666f\u751f\u6001\u6b65\u9053\u7167\u7247", "caption_en": "Photographs of the constructed birdscape trail in Huanglong Park"}
    ]
  },
  {
    "id": "wang-zisong",
    "photo": "images/photo-faculty-5582.webp",
    "name_zh": "\u6c6a\u6ecb\u677e",
    "name_en": "Wang Zisong",
    "title_zh": "\u526f\u6559\u6388\u3001\u535a\u58eb\u751f\u5bfc\u5e08",
    "title_en": "Associate Professor, PhD Supervisor",
    "bio_zh": "\u6c6a\u6ecb\u677e\uff0c\u526f\u6559\u6388\u3001\u535a\u58eb\u751f\u5bfc\u5e08\uff0c\u957f\u671f\u4ee5\u6765\u4ece\u4e8b\u53ef\u6301\u7eed\u4f4e\u78b3\u8bbe\u8ba1\uff0c\u5728\u7eff\u8272\u6821\u56ed\u3001\u751f\u6001\u57ce\u5e02\u89c4\u5212\u3001\u6ee8\u6c34\u57ce\u5e02\u8bbe\u8ba1\u3001\u7eff\u8272\u5efa\u7b51\u8bbe\u8ba1\u7b49\u65b9\u9762\u5f00\u5c55\u7814\u7a76\u53ca\u5b9e\u8df5\u5de5\u4f5c\u3002\u4e3b\u6301\u53ca\u53c2\u4e0e\u591a\u9879\u56fd\u5bb6\u7ea7\u3001\u7701\u90e8\u7ea7\u3001\u4e2d\u592e\u9ad8\u6821\u7b49\u79d1\u7814\u9879\u76ee\u3002\u76ee\u524d\u4e3a\u4e2d\u56fd\u57ce\u5e02\u79d1\u5b66\u7814\u7a76\u4f1a\u7eff\u8272\u5efa\u7b51\u4e0e\u8282\u80fd\u4e13\u4e1a\u59d4\u5458\u4f1a\u59d4\u5458\uff0c\u4e2d\u56fd\u57ce\u79d1\u4f1a\u7eff\u8272\u5efa\u7b51\u4e0e\u8282\u80fd\u4e13\u4e1a\u59d4\u5458\u4f1a\u7eff\u8272\u6821\u56ed\u5b66\u7ec4\u79d8\u4e66\u957f\u3002\u4f5c\u4e3a\u6307\u5bfc\u8001\u5e08\u6307\u5bfc\u5b66\u751f\u591a\u6b21\u83b7\u56fd\u9645\u57ce\u5e02\u8bbe\u8ba1\u53ca\u666f\u89c2\u8bbe\u8ba1\u5927\u8d5b\u591a\u4e2a\u5956\u9879\uff0c\u83b7\u5f97\u56fd\u5bb6\u7eff\u8272\u5efa\u7b51\u4e8c\u661f\u8bbe\u8ba1\u6807\u8bc6\u53ca\u8fd0\u884c\u6807\u8bc6\u591a\u9879\u3002",
    "bio_en": "",
    "tags": ["Ecology", "Green Campus", "Green Building", "Urban Planning"],
    "achievements": [
      {
        "name_zh": "\u300a\u7eff\u8272\u6821\u56ed\u8bc4\u4ef7\u6807\u51c6\u300bGB/T51356-2019 \u56fd\u5bb6\u6807\u51c6\u7f16\u5236",
        "name_en": "",
        "description_zh": "\u4f5c\u4e3a\u56fd\u5bb6\u6807\u51c6\u300a\u7eff\u8272\u6821\u56ed\u8bc4\u4ef7\u6807\u51c6\u300bGB/T 51356-2019\u4f4d\u5217\u7b2c\u4e09\u4f4d\u7684\u4e3b\u8981\u7f16\u5199\u4eba\uff0c\u8be5\u6807\u51c6\u6db5\u76d6\u4e2d\u5c0f\u5b66\u3001\u804c\u4e1a\u5b66\u6821\u3001\u9ad8\u6821\u7eff\u8272\u6821\u56ed\u5efa\u8bbe\u8bc4\u4f30\u5185\u5bb9\uff0c\u4e8e2019\u5e7410\u67081\u65e5\u5b9e\u65bd\u3002\u540c\u65f6\u4f5c\u4e3a\u884c\u4e1a\u6807\u51c6CSUS/GBC 04-2013\u7684\u7b2c\u4e09\u7f16\u5199\u4eba\u53ca\u6807\u51c6\u534f\u8c03\u4eba\uff0c\u8be5\u6807\u51c6\u4e8e2013\u5e744\u67081\u65e5\u5b9e\u65bd\u3002",
        "description_en": ""
      },
      {
        "name_zh": "\u300a\u7eff\u8272\u6821\u56ed\u4e0e\u672a\u6765\u300b\u7cfb\u5217\u6559\u6750\u53c2\u7f16",
        "name_en": "",
        "description_zh": "\u53c2\u7f16\u4e2d\u56fd\u9996\u90e8\u201c\u4e2d\u56fd\u7eff\u8272\u6821\u56ed\u53ca\u7eff\u8272\u5efa\u7b51\u8282\u80fd\u77e5\u8bc6\u201d\u5c0f\u5b66\u81f3\u5927\u5b665\u672c\u7cfb\u5217\u6559\u6750\u300a\u7eff\u8272\u6821\u56ed\u4e0e\u672a\u6765\u300b\uff081-5\u518c\uff09\uff0c\u7531\u5434\u5fd7\u5f3a\u9662\u58eb\u4e3b\u7f16\uff0c\u9488\u5bf9\u4e0d\u540c\u5b66\u6bb5\u8bbe\u7f6e\u57fa\u51c6\u4e3b\u9898\u30022015\u5e74\u7531\u4e2d\u56fd\u5efa\u7b51\u5de5\u4e1a\u51fa\u7248\u793e\u6b63\u5f0f\u51fa\u7248\u3002",
        "description_en": ""
      },
      {
        "name_zh": "\u65e0\u9521\u5e02\u4e94\u7231\u5c0f\u5b66\u96ea\u67ab\u5206\u6821",
        "name_en": "",
        "description_zh": "2021\u5e74\u4e3b\u6301\u8bbe\u8ba1\u7684\u65e0\u9521\u5e02\u4e94\u7231\u5c0f\u5b66\u96ea\u67ab\u5206\u6821\uff08\u5df2\u5efa\u6210\uff09\u83b7\u7b2c\u5341\u516d\u5c4a\u56ed\u51b6\u676f\u56fd\u9645\u7ade\u8d5b\u56fd\u9645\u5efa\u7b51\u5956\u91d1\u5956\u3001\u5e76\u83b7\u56fd\u5bb6\u4e8c\u661f\u7eff\u8272\u5efa\u7b51\u8ba4\u8bc1\u3002\u5b66\u6821\u7528\u5730\u9762\u79ef\u7ea633342\u5e73\u65b9\u7c73\uff0c\u5efa\u7b51\u9762\u79ef\u7ea633272\u5e73\u65b9\u7c73\u3002",
        "description_en": ""
      }
    ],
    "courses": [
      {"name_zh": "\u8bbe\u8ba1\u6280\u672f1", "name_en": "Design Technology 1", "description_zh": "\u672c\u79d1\u751f\u8bfe\u7a0b", "description_en": "Undergraduate course"},
      {"name_zh": "\u8bbe\u8ba1\u5b9e\u8df5\u7814\u7a76\u4e13\u98982\uff08\u534f\u540c\u8bbe\u8ba1\uff09", "name_en": "Design Practice Research Seminar 2 (Collaborative Design)", "description_zh": "\u7855\u58eb\u751f\u8bfe\u7a0b", "description_en": "Graduate course"}
    ],
    "gallery": [
      {"src": "images/faculty-4879.webp", "caption_zh": "\u65e0\u9521\u5e02\u4e94\u7231\u5c0f\u5b66\u96ea\u67ab\u5206\u6821\u62a5\u544a\u5385", "caption_en": ""},
      {"src": "images/faculty-4050.webp", "caption_zh": "\u65e0\u9521\u5e02\u4e94\u7231\u5c0f\u5b66\u96ea\u67ab\u5206\u6821\u5185\u666f", "caption_en": ""},
      {"src": "images/faculty-8674.webp", "caption_zh": "\u65e0\u9521\u5e02\u4e94\u7231\u5c0f\u5b66\u96ea\u67ab\u5206\u6821\u83b7\u7b2c\u5341\u516d\u5c4a\u56ed\u51b6\u676f\u56fd\u9645\u7ade\u8d5b\u56fd\u9645\u5efa\u7b51\u5956\u91d1\u5956", "caption_en": ""},
      {"src": "images/faculty-8724.webp", "caption_zh": "\u65e0\u9521\u5e02\u4e94\u7231\u5c0f\u5b66\u96ea\u67ab\u5206\u6821\u83b7\u56fd\u5bb6\u7eff\u8272\u5efa\u7b51\u4e8c\u661f\u8ba4\u8bc1", "caption_en": ""}
    ]
  },
  {
    "id": "lou-yongqi",
    "photo": "images/photo-yongqi-lou.webp",
    "name_zh": "\u5a04\u6c38\u7426",
    "name_en": "Yongqi Lou",
    "title_zh": "\u6559\u6388\u3001\u535a\u58eb\u751f\u5bfc\u5e08",
    "title_en": "Professor, PhD Supervisor",
    "bio_zh": "\u5a04\u6c38\u7426\uff0c\u6559\u6388\u3001\u535a\u58eb\u751f\u5bfc\u5e08\uff0c\u73b0\u4efb\u4e0a\u6d77\u5de5\u7a0b\u6280\u672f\u5927\u5b66\u6821\u957f\uff0c\u540c\u6d4e\u5927\u5b66\u8bbe\u8ba1\u5b66\u79d1\u5e26\u5934\u4eba\u3002\u957f\u671f\u81f4\u529b\u4e8e\u53ef\u6301\u7eed\u8bbe\u8ba1\u4e0e\u793e\u4f1a\u521b\u65b0\u8bbe\u8ba1\u7684\u6559\u5b66\u3001\u7814\u7a76\u4e0e\u516c\u5171\u5b9e\u8df5\u3002\u4e3b\u5f20\u8bbe\u8ba1\u5e94\u8d85\u8d8a\u4f20\u7edf\u5f62\u5f0f\u4e0e\u529f\u80fd\u8303\u7574\uff0c\u8fdb\u5165\u771f\u5b9e\u4e16\u754c\u56de\u5e94\u751f\u6001\u3001\u793e\u4f1a\u4e0e\u6cbb\u7406\u7684\u7cfb\u7edf\u6027\u6311\u6218\u3002\u4ed6\u63d0\u51fa\u201c\u8bbe\u8ba1\u9a71\u52a8\u521b\u65b0\u201d\u7406\u5ff5\uff0c\u53d1\u8d77\u201c\u8bbe\u8ba1\u4e30\u6536\u201d\uff08Design Harvests\uff09\u9879\u76ee\uff0c\u4ee5\u53c2\u4e0e\u5f0f\u8bbe\u8ba1\u65b9\u6cd5\u4fc3\u8fdb\u57ce\u4e61\u4e92\u52a8\u4e0e\u793e\u533a\u53ef\u6301\u7eed\u53d1\u5c55\uff1b\u521b\u5efa\u201cNICE 2035\u201d\u793e\u533a\u521b\u65b0\u5e73\u53f0\u3002\u5165\u9009\u6559\u80b2\u90e8\u201c\u957f\u6c5f\u5b66\u8005\u5956\u52b1\u8ba1\u5212\u201d\u7279\u8058\u6559\u6388\uff0c\u5f53\u9009\u745e\u5178\u7687\u5bb6\u5de5\u7a0b\u79d1\u5b66\u9662\u9662\u58eb\uff0c2023\u5e74\u83b7\u82f1\u56fd\u7687\u5bb6\u827a\u672f\u5b66\u9662\u8363\u8a89\u535a\u58eb\u3002\u62c5\u4efb\u300aShe Ji: The Journal of Design, Economics and Innovation\u300b\u6267\u884c\u4e3b\u7f16\u3002\u540c\u6d4e\u5927\u5b66\u590d\u6742\u793e\u4f1a\u6280\u672f\u7cfb\u7edf\u8bbe\u8ba1\u7814\u7a76\u4e2d\u5fc3\uff08SustainX\uff09\u3001\u793e\u4f1a\u521b\u65b0\u548c\u53ef\u6301\u7eed\u8bbe\u8ba1\u5b9e\u9a8c\u5ba4\uff08Tongji DESIS\uff09\u3001\u540c\u6d4e\u5927\u5b66-\u9ebb\u7701\u7406\u5de5\u5b66\u9662\u4e0a\u6d77\u57ce\u5e02\u79d1\u5b66\u5b9e\u9a8c\u5ba4\u4e2d\u5fc3\u5e26\u5934\u4eba\u3002",
    "bio_en": "Yongqi Lou is a Professor and PhD supervisor, currently serving as President of Shanghai University of Engineering Science and the disciplinary leader of Design at Tongji University. His work focuses on sustainable design and social innovation through teaching, research, and public practice. Lou advocates that design should move beyond traditional concerns with form and function to actively engage with real-world systemic challenges. He initiated the Design Harvests project and founded the NICE 2035 community innovation platform. Lou was selected as a Distinguished Professor of the Changjiang Scholars Program and elected a Fellow of the Royal Swedish Academy of Engineering Sciences. In 2023, he received an Honorary Doctorate from the Royal College of Art. He serves as Executive Editor-in-Chief of She Ji: The Journal of Design, Economics and Innovation. He leads SustainX, the Tongji DESIS Lab, and the Tongji\u2013MIT Shanghai City Science Lab.",
    "tags": ["Sustainable Design", "Social Innovation", "Systemic Design", "Participatory Design", "Ecology"],
    "achievements": [
      {
        "name_zh": "\u8bbe\u8ba1\u4e30\u6536",
        "name_en": "Design Harvests",
        "description_zh": "\u8bbe\u8ba1\u4e30\u6536\u662f\u4e00\u4e2a\u4ee5\u8bbe\u8ba1\u9a71\u52a8\u57ce\u4e61\u4e92\u52a8\u4e0e\u793e\u533a\u53d1\u5c55\u7684\u793e\u4f1a\u521b\u65b0\u9879\u76ee\u3002\u9879\u76ee\u901a\u8fc7\u53c2\u4e0e\u5f0f\u8bbe\u8ba1\u65b9\u6cd5\uff0c\u5c06\u57ce\u5e02\u521b\u610f\u8d44\u6e90\u4e0e\u4e61\u6751\u4f20\u7edf\u667a\u6167\u76f8\u7ed3\u5408\uff0c\u56f4\u7ed5\u519c\u4e1a\u751f\u4ea7\u3001\u624b\u5de5\u827a\u590d\u5174\u4e0e\u793e\u533a\u8425\u9020\u5f00\u5c55\u534f\u540c\u5b9e\u8df5\uff0c\u63a8\u52a8\u57ce\u4e61\u4e4b\u95f4\u5f62\u6210\u4e92\u8865\u5171\u751f\u7684\u53d1\u5c55\u6a21\u5f0f\u3002",
        "description_en": "Design Harvests is a social innovation initiative that uses design to foster interaction between urban and rural communities. Through participatory design approaches, the project connects urban creative resources with rural traditional knowledge, focusing on collaborative practices in sustainable agriculture, craft revitalization, and community building."
      },
      {
        "name_zh": "NICE 2035 \u793e\u533a\u521b\u65b0\u5e73\u53f0",
        "name_en": "NICE 2035 Community Innovation Platform",
        "description_zh": "NICE 2035\u662f\u4e00\u4e2a\u9762\u5411\u672a\u6765\u751f\u6d3b\u65b9\u5f0f\u7684\u793e\u533a\u7ea7\u793e\u4f1a\u521b\u65b0\u5b9e\u9a8c\u5e73\u53f0\u3002\u9879\u76ee\u4ee5\u201c\u8bbe\u8ba1\u9a71\u52a8\u521b\u65b0\u201d\u4e3a\u6838\u5fc3\u7406\u5ff5\uff0c\u6c47\u805a\u9ad8\u6821\u3001\u4f01\u4e1a\u3001\u653f\u5e9c\u4e0e\u793e\u533a\u5c45\u6c11\uff0c\u5728\u771f\u5b9e\u793e\u533a\u573a\u666f\u4e2d\u5f00\u5c55\u8de8\u754c\u534f\u4f5c\uff0c\u63a2\u7d22\u53ef\u6301\u7eed\u7684\u4ea7\u54c1\u3001\u670d\u52a1\u4e0e\u7cfb\u7edf\u89e3\u51b3\u65b9\u6848\u3002",
        "description_en": "NICE 2035 is a community-based social innovation platform that explores future lifestyles through design-driven innovation. It brings together universities, companies, government agencies, and local residents to collaborate within real community environments, incubating sustainable products, services, and systems."
      },
      {
        "name_zh": "\u201c\u8bbe\u8ba1\u65e0\u754c \u751f\u751f\u4e0d\u606f\u201d\u4e3b\u9898\u5c55",
        "name_en": "\"Design Without Boundaries, Design for Sustainability\" Exhibition",
        "description_zh": "\u5728\u4e16\u754c\u8bbe\u8ba1\u4e4b\u90fd\u5927\u4f1a\u6846\u67b6\u4e0b\u7b56\u5212\u7684\u91cd\u8981\u5c55\u89c8\u9879\u76ee\u3002\u5c55\u89c8\u4ee5\u8bbe\u8ba1\u8de8\u8d8a\u5b66\u79d1\u4e0e\u884c\u4e1a\u8fb9\u754c\u4e3a\u6838\u5fc3\u89c6\u89d2\uff0c\u901a\u8fc7\u591a\u6837\u5316\u6848\u4f8b\u4e0e\u5b9e\u8df5\uff0c\u5448\u73b0\u8bbe\u8ba1\u5728\u751f\u6001\u4fdd\u62a4\u3001\u793e\u4f1a\u521b\u65b0\u4e0e\u4ea7\u4e1a\u8f6c\u578b\u4e2d\u7684\u79ef\u6781\u4f5c\u7528\u3002",
        "description_en": "Curated within the framework of the World Design Cities Conference (WDCC), the exhibition highlights how design transcends disciplinary and industrial boundaries to address ecological, social, and economic challenges, encouraging the public to recognize the broader value of design."
      }
    ],
    "courses": [],
    "gallery": []
  },
  {
    "id": "lu-wen",
    "photo": "images/photo-lu-wen.webp",
    "name_zh": "\u5362\u96ef",
    "name_en": "Lu Wen",
    "title_zh": "\u52a9\u7406\u7814\u7a76\u5458",
    "title_en": "Associate Research Fellow",
    "bio_zh": "\u6bd5\u4e1a\u4e8e\u90fd\u7075\u7406\u5de5\u5927\u5b66\uff0c\u83b7\u7ba1\u7406\u3001\u751f\u4ea7\u4e0e\u8bbe\u8ba1\u5de5\u5b66\u535a\u58eb\u5b66\u4f4d\u3002\u4ece\u4e8b\u57fa\u4e8e\u7cfb\u7edf\u8bbe\u8ba1\u65b9\u6cd5\u7684\u8de8\u5b66\u79d1\u7814\u7a76\uff0c\u7814\u7a76\u65b9\u5411\u6db5\u76d6\u53ef\u6301\u7eed\u533b\u7597\u7cfb\u7edf\u3001\u751f\u6001\u7cfb\u7edf\u4fdd\u62a4\u4ee5\u53ca\u4f01\u4e1a\u7684\u521b\u65b0\u8f6c\u578b\u7b49\u9886\u57df\u3002\u5728\u53ef\u6301\u7eed\u533b\u7597\u65b9\u9762\uff0c\u7814\u7a76\u805a\u7126\u4e8e\u4e2d\u610f\u4e24\u56fd\u7684\u8001\u5e74\u4eba\u793e\u533a\u62a4\u7406\u4f53\u7cfb\u3001\u53ef\u6301\u7eed\u533b\u7597\u6559\u80b2\u4e0e\u57f9\u8bad\u3001\u4ee5\u53ca\u533b\u7597\u673a\u6784\u5e9f\u5f03\u7269\u7cfb\u7edf\uff1b\u5728\u751f\u6001\u7cfb\u7edf\u4fdd\u62a4\u65b9\u9762\uff0c\u7814\u7a76\u5185\u5bb9\u5305\u62ec\u4e0a\u6d77\u957f\u6c5f\u53e3\u6f6e\u6c50\u5e9f\u7269\u7cfb\u7edf\u8c03\u67e5\u3001\u9752\u6d77\u957f\u6c5f\u6e90\u5730\u533a\u7684\u5e9f\u7269\u4e0e\u6c61\u6c34\u5904\u7406\u7cfb\u7edf\u3001\u91ce\u751f\u52a8\u7269\u591a\u6837\u6027\u4e0e\u6816\u606f\u5730\u4fdd\u62a4\u7b49\u8bae\u9898\u3002",
    "bio_en": "Graduated from Politecnico di Torino with a PhD in Management, Production and Design Engineering. Her work focuses on interdisciplinary research grounded in Systemic Design methodologies, with research interests spanning sustainable healthcare systems, ecosystem conservation, and innovation-driven transformation in enterprises. In sustainable healthcare, her research focuses on community-based elderly care systems in China and Italy, sustainable healthcare education, and healthcare waste systems. In ecosystem conservation, her work includes the tidal waste system at the Yangtze Estuary, waste management systems in the Yangtze River source region, and wildlife biodiversity conservation.",
    "tags": ["Systemic Design", "Ecosystem Conservation", "Sustainable Healthcare", "Elderly Care", "Zero Waste", "Ecology"],
    "achievements": [
      {
        "name_zh": "\u957f\u6c5f\u53e3\u6f6e\u6c50\u5e9f\u7269\u7cfb\u7edf\u7814\u7a76",
        "name_en": "Systemic Research on Tidal Waste at the Yangtze Estuary",
        "description_zh": "\u9879\u76ee\u6839\u690d\u4e8e\u4e0a\u6d77\u5434\u6dc2\u70ae\u53f0\u6e7e\u56fd\u5bb6\u6e7f\u5730\u516c\u56ed\uff0c\u8fd0\u7528\u7cfb\u7edf\u8bbe\u8ba1\u65b9\u6cd5\u5e94\u5bf9\u5e9f\u5f03\u7269\u968f\u6f6e\u6c50\u6d8c\u5165\u6cb3\u6d41\u7684\u6311\u6218\u30022025\u5e7411\u6708\u83b72025\u5e74\u5510\u00b7\u8bfa\u66fc\u8bbe\u8ba1\u7ec4\u7ec7\u5956\u3002",
        "description_en": "Rooted in the Wusong Paotaiwan National Wetland Park, this project applies a Systemic Design approach to address the challenge of waste being carried into the river system by tidal movements. The project received the 2025 Don Norman Design Organisation Award in November 2025."
      },
      {
        "name_zh": "\u7cfb\u7edf\u8bbe\u8ba1\u4fc3\u8fdb\u53ef\u6301\u7eed\u793e\u533a\u7167\u62a4\u2014\u2014\u4ee5\u90fd\u7075\u4e0e\u4e0a\u6d77\u4e3a\u4f8b",
        "name_en": "Systemic Design for Sustainable Community Care: A Comparison between Turin and Shanghai",
        "description_zh": "\u5bf9\u4e0a\u6d77\u9759\u5b89\u533a\u4e0e\u90fd\u7075ASL TO3\u793e\u533a\u8001\u5e74\u62a4\u7406\u6a21\u5f0f\u8fdb\u884c\u6bd4\u8f83\u7814\u7a76\uff0c\u63a2\u7d22\u53ef\u6301\u7eed\u793e\u533a\u7167\u62a4\u4f53\u7cfb\u7684\u521b\u65b0\u8def\u5f84\u3002\u7814\u7a76\u63d0\u51fa\u201c\u533b\u517b\u4e94\u5e8a\u8054\u52a8\u201d\u6574\u5408\u7167\u62a4\u6a21\u5f0f\u3002",
        "description_en": "A comparative study of community-based elderly care models in Jing'an District, Shanghai, and A.S.L. TO3 in Turin. The study proposes an integrated \"Five-bed Linkage\" care model, promoting collaboration between healthcare and social services."
      }
    ],
    "courses": [],
    "gallery": [
      {"src": "images/faculty-1602.webp", "caption_zh": "\u6982\u5ff5\u6a21\u5f0f", "caption_en": ""},
      {"src": "images/faculty-5916.webp", "caption_zh": "\u9759\u5b89\u793e\u533a\u7167\u62a4\u65b0\u201c\u4e94\u5e8a\u8054\u52a8\u201d\u7167\u62a4\u6a21\u5f0f\u5229\u76ca\u76f8\u5173\u8005\u56fe\u8c31", "caption_en": ""},
      {"src": "images/faculty-2020.webp", "caption_zh": "\u4e2d\u56fd\u3001\u610f\u5927\u5229\u548c\u65e5\u672c\u533b\u7597\u653f\u7b56\u53d1\u5c55\u7684\u91cc\u7a0b\u7891", "caption_en": ""},
      {"src": "images/faculty-7160.webp", "caption_zh": "\u6587\u732e\u7efc\u8ff0\u7ed3\u679c\u7684\u53ef\u89c6\u5316\u5448\u73b0", "caption_en": ""},
      {"src": "images/asl-to.webp", "caption_zh": "A.S.L. TO3\u793e\u533a\u62a4\u7406\u8de8\u5c3a\u5ea6\u6a21\u578b", "caption_en": ""}
    ]
  }
]

# Write with json.dumps to ensure proper escaping
output = "window.__SITE_DATA__ = " + json.dumps(data, ensure_ascii=False, indent=2) + ";\n"
with open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(output)

print(f"Written {len(data)} faculty members to {DATA_JS}")

# Validate
with open(DATA_JS, "r") as f:
    content = f.read()
content = content.replace("window.__SITE_DATA__ = ", "").rstrip().rstrip(";")
validated = json.loads(content)
print(f"Validated: {len(validated)} faculty members")
for f_data in validated:
    print(f"  {f_data['name_zh']}: {len(f_data['achievements'])} achievements, {len(f_data['courses'])} courses, {len(f_data['gallery'])} gallery")

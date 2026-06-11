#!/usr/bin/env python3
"""Update data.js with full text extracted from Word documents."""
import json, os

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(SITE_DIR, 'data.js')

with open(DATA_FILE, 'r', encoding='utf-8') as f:
    content = f.read()
# Extract the JSON array
json_str = content.split('=', 1)[1].strip().rstrip(';').strip()
data = json.loads(json_str)

# Build a lookup by id
by_id = {d['id']: d for d in data}

# ─── LOU YONGQI ───
lou = by_id['lou-yongqi']
lou['achievements'] = [
    {
        "name_zh": "设计丰收（Design Harvests）",
        "name_en": "Design Harvests",
        "description_zh": "设计丰收（Design Harvests）是一个以设计驱动城乡互动与社区发展的社会创新项目。项目通过参与式设计方法，将城市创意资源与乡村传统智慧相结合，围绕农业生产、手工艺复兴与社区营造开展协同实践。通过设计介入真实场景，激活地方文化与社会网络，探索可持续的生产与生活方式，推动城乡之间形成互补共生的发展模式，并为乡村振兴与社区可持续发展提供新的设计路径与实践案例。",
        "description_en": "Design Harvests is a social innovation initiative that uses design to foster interaction between urban and rural communities and support community development. Through participatory design approaches, the project connects urban creative resources with rural traditional knowledge. It focuses on collaborative practices in sustainable agriculture, craft revitalization, and community building. By introducing design into real-life contexts, the initiative activates local culture, skills, and social networks while exploring sustainable ways of production and living. Design Harvests aims to develop new models of urban\u2013rural symbiosis and to provide practical design-driven approaches for rural revitalization and long-term community sustainability."
    },
    {
        "name_zh": "NICE 2035 社区创新平台",
        "name_en": "NICE 2035 Community Innovation Platform",
        "description_zh": "NICE 2035是一个面向未来生活方式的社区级社会创新实验平台。项目以\u201c设计驱动创新\u201d为核心理念，汇聚高校、企业、政府与社区居民，在真实社区场景中开展跨界协作。通过设计实验、原型孵化与公共参与，探索可持续的产品、服务与系统解决方案。平台关注城市微更新、社区治理与社会创新实践，致力于在日常生活空间中构建开放协同的创新生态，为未来城市社区的发展提供新的方法与实践路径。",
        "description_en": "NICE 2035 is a community-based social innovation platform that explores future lifestyles through design-driven innovation. The initiative brings together universities, companies, government agencies, and local residents to collaborate within real community environments. Through design experiments, prototyping, and public participation, the platform incubates sustainable products, services, and systems. NICE 2035 focuses on urban micro-renewal, community governance, and everyday innovation practices. By creating an open and collaborative innovation ecosystem embedded in daily life, it explores new approaches to shaping future urban communities and demonstrates how design can serve as a catalyst for social innovation and sustainable urban development."
    },
    {
        "name_zh": "\u201c设计无界 生生不息\u201d主题展",
        "name_en": "\u201cDesign Without Boundaries, Design for Sustainability\u201d Exhibition",
        "description_zh": "\u201c设计无界 生生不息\u201d主题展是在世界设计之都大会（WDCC）框架下策划的重要展览项目。展览以设计跨越学科与行业边界为核心视角，通过多样化案例与实践，呈现设计在生态保护、社会创新与产业转型中的积极作用。展览强调设计作为连接技术、文化与社会的重要媒介，引导公众理解设计在可持续发展中的价值，并推动设计从单一产品创造走向系统性创新与社会变革。",
        "description_en": "Curated within the framework of the World Design Cities Conference (WDCC), the exhibition highlights how design transcends disciplinary and industrial boundaries to address ecological, social, and economic challenges. Through diverse cases and design practices, it demonstrates the role of design in environmental sustainability, social innovation, and industrial transformation. The exhibition presents design as a bridge connecting technology, culture, and society, while encouraging the public to recognize the broader value of design. It aims to promote the understanding of design not only as product creation but also as a driver of systemic innovation and societal change."
    }
]

# ─── QINGFAN AN ───
an = by_id['qingfan-an']
an['bio_zh'] = "欧盟玛丽\u00b7居里学者（Marie Sk\u0142odowska-Curie Fellow），欧洲呼吸协会成员。先后在英国利物浦大学与英国皇家艺术学院获得工业设计学士及设计研究硕士学位，后于瑞典于默奥大学攻读博士，作为欧盟玛丽居里创新训练网络项目 Health CASCADE 的核心成员，获得医学博士学位。在《Design Studies》《CoDesign》等国际高水平期刊发表学术论文20余篇，并在 HCII、工程与产品设计教育会议、国际设计会议、美国医学信息学协会年会等国际重要学术会议作口头报告。担任 ACM CHI、国际设计会议、E&PDE 等多个国际会议审稿人，并曾担任 E&PDE 分会场主席，同时为多本国际学术期刊担任审稿人。研究方向聚焦设计研究与医疗健康交叉领域，涵盖 AI 赋能医疗产品设计、移动医疗、慢性病自我管理干预设计、医疗保健领域共同创造及系统设计等。"
an['achievements'] = [
    {
        "name_zh": "医疗保健领域的过渡设计模型",
        "name_en": "Transition Design Model for Healthcare",
        "description_zh": "发展了医疗保健领域的过渡设计模型（Transition Design），用于复杂医疗系统问题的系统化解决。该模型不仅提供可操作的设计策略，还制定了检验标准，为设计学进入医疗保健领域提供了可信赖的科研路径。研究成果发表于 Design Studies（2025），被同行广泛引用。",
        "description_en": "Developed a Transition Design model for healthcare, aimed at systematically addressing complex problems in healthcare systems. This model not only provides actionable design strategies but also establishes evaluation criteria, offering a credible research pathway for integrating design research into the healthcare domain. Published in Design Studies, 2025; widely cited by peers."
    },
    {
        "name_zh": "医疗方案的生态方法（Ecology of Design Briefs）",
        "name_en": "Ecology of Design Briefs",
        "description_zh": "提出并设计了医疗方案生态方法（Ecology of Design Briefs），作为促进医疗干预设计与实施的具体方法论。该方法将共创设计与系统设计相结合，为医疗干预方案的开发提供结构化指导，推动设计研究在医疗健康中的应用。研究成果发表于 CoDesign（2025）。",
        "description_en": "Proposed an approach named Ecology of Design Briefs, serving as a practical methodology to support the design and implementation of healthcare interventions. By combining co-creation and systemic thinking, this approach provides structured guidance for developing intervention programs and advances the application of design research in healthcare. Published in CoDesign, 2025."
    }
]

# ─── ZHU XIAOCUN ───
zx = by_id['zhu-xiaocun']
zx['bio_zh'] = "朱小村，同济大学设计创意学院副教授。她受过系统的建筑学训练，毕业于东南大学（建筑学学士、硕士），后于哈佛大学设计研究生院取得设计研究硕士学位。2002年加入同济大学，先后任教于建筑与城市规划学院与设计创意学院。她长期致力于可持续设计、环境设计与系统思维领域的研究与教学，聚焦于在快速变化背景下探寻人类社会真正的可持续性。她擅长在整体语境中观察问题、寻求综合性解决方案，致力于推动从\u201c减少伤害\u201d向创造\u201c更多善意\u201d的转型与创新。她曾在意大利米兰理工大学、瑞典隆德大学、瑞典国立艺术与设计大学、清华大学、中央美术学院、东南大学等高校担任访问教授或演讲嘉宾。"
zx['bio_en'] = "Zhu Xiaocun is an Associate Professor at the College of Design and Innovation, Tongji University. Trained systematically in architecture, she received her Bachelor and Master of Architecture from Southeast University in China, and later earned a Master of Design Studies from the Harvard Graduate School of Design. She joined Tongji University in 2002 and has taught at the College of Architecture and Urban Planning and the College of Design and Innovation. Her long-term research and teaching focus on sustainable design, environmental design, and systems thinking, with an emphasis on pursuing genuine sustainability for human society in the context of rapid change. Skilled at observing issues and seeking integrated solutions within holistic contexts, she is dedicated to advancing the transition from \"reducing harm\" to creating \"more good.\" She has been invited as a visiting professor or guest speaker at several institutions, including Politecnico di Milano in Italy, Lund University and Konstfack University of Arts, Crafts and Design in Sweden, and Tsinghua University, Central Academy of Fine Arts, and Southeast University in China."
zx['courses'] = [
    {
        "name_zh": "可持续设计理念",
        "name_en": "Sustainability Consciousness",
        "description_zh": "同济大学设计创意学院面向全体本科生的必修课。从身边的日常现象出发，以跨学科思辨洞察设计如何超越\u201c减少伤害\u201d，创造更多善意。课程旨在培养学生系统性思维与可持续理念，成为具备可持续意识的设计师。",
        "description_en": "Compulsory course for all undergraduates at the College of Design and Innovation, Tongji University. Starting from everyday phenomena, this course uses cross-disciplinary inquiry to examine how design can move beyond \"reducing harm\" and create more good. It aims to cultivate students' systemic thinking and sustainable mindset, shaping designers with genuine sustainability awareness."
    },
    {
        "name_zh": "可持续（再生）设计",
        "name_en": "Regenerative Design for Sustainability",
        "description_zh": "同济大学设计创意学院全英文研究生课程。从系统思维出发，看见更大图景，探索全球议题与本地解决方案。在跨文化交流中重新定义设计师角色，让设计真正\u201c向好而生\u201d。",
        "description_en": "English-taught graduate course at the College of Design and Innovation, Tongji University. Adopting a systems thinking approach to see the bigger picture, this course explores global issues and local solutions. It redefines the role of designers through cross-cultural exchange, enabling design to truly \"grow toward the good.\""
    }
]

# ─── LU WEN ───
lw = by_id['lu-wen']
lw['achievements'] = [
    {
        "name_zh": "长江口潮汐废物系统研究",
        "name_en": "Systemic Research on Tidal Waste at the Yangtze Estuary",
        "description_zh": "项目根植于上海吴淞炮台湾国家湿地公园，运用系统设计方法应对废弃物随潮汐涌入河流的挑战。在零废弃社区的建设过程中，注重包容性与社区赋权。2025年11月，该项目获得2025年唐\u00b7诺曼设计组织奖。",
        "description_en": "Rooted in the Wusong Paotaiwan National Wetland Park, this project applies a Systemic Design approach to address the challenge of waste being carried into the river system by tidal movements. In the process of developing zero-waste communities, the project places strong emphasis on inclusivity and community empowerment. In November 2025, the project received the 2025 Don Norman Design Organisation Award."
    },
    {
        "name_zh": "系统设计促进可持续社区照护\u2014\u2014以都灵与上海为例",
        "name_en": "Systemic Design for Sustainable Community Care: A Comparison between Turin and Shanghai",
        "description_zh": "本研究对上海静安区与都灵ASL TO3社区老年护理模式进行比较研究，探索可持续社区照护体系的创新路径。研究提出\u201c医养五床联动\u201d整合照护模式，促进医疗与社会服务协同，提升老年人社区照护质量与可持续性。",
        "description_en": "This research presents a comparative study of community-based elderly care models in Jing'an District, Shanghai, and A.S.L. TO3 in Turin, exploring innovative pathways towards more sustainable community care systems. The study proposes an integrated \"Five-bed Linkage\" care model, promoting collaboration between healthcare and social services, while enhancing the quality and sustainability of community care for older adults."
    }
]

# ─── ZHANG SHUAI ───
zs = by_id['zhang-shuai']
zs['courses'] = [
    {
        "name_zh": "可持续思维",
        "name_en": "Sustainable Thinking",
        "description_zh": "面向研究生的专业课程，课程内容侧重于可持续问题的思考方式和研究范式，培养学生从经济学、管理学和设计学的多学科视角理解可持续发展问题的能力。",
        "description_en": "A specialized course for graduate students that focuses on the ways of thinking and research paradigms for addressing sustainability issues, cultivating students' ability to understand sustainable development from multidisciplinary perspectives of economics, management, and design."
    },
    {
        "name_zh": "可持续发展理论与研究方法",
        "name_en": "Theory and Research Methods of Sustainable Development",
        "description_zh": "面向研究生的专业课程，课程内容侧重于可持续发展的\u201c宏观\u201d理论与方法，系统讲授可持续发展的核心理论框架和前沿研究方法。",
        "description_en": "A specialized course for graduate students that emphasizes the 'macro-level' theories and methods of sustainable development, systematically teaching the core theoretical frameworks and cutting-edge research methodologies."
    },
    {
        "name_zh": "可持续发展经济学前沿研究",
        "name_en": "Advanced Research on the Economics of Sustainable Development",
        "description_zh": "面向研究生的专业课程，课程内容侧重于讨论可持续发展经济学领域的最新研究问题、方法、结论等，紧跟国际学术前沿动态。",
        "description_en": "A specialized course for graduate students that examines the latest research questions, methodologies, and findings in the field of sustainable development economics, keeping pace with international academic frontiers."
    },
    {
        "name_zh": "资源环境经济学",
        "name_en": "Resource and Environmental Economics",
        "description_zh": "面向研究生的专业课程，课程内容侧重于从经济学的视角理解和解决资源环境的难题和困境，培养学生运用经济学分析方法解决实际环境问题的能力。",
        "description_en": "A specialized course for graduate students that approaches the understanding and resolution of resource and environmental challenges from an economic perspective, developing students' ability to apply economic analysis to solve real-world environmental problems."
    },
    {
        "name_zh": "可持续设计：思维和案例",
        "name_en": "Sustainable Design: Thinking and Cases",
        "description_zh": "面向研究生的专业课程，课程内容侧重于可持续发展的理论和方法在材料、商品、服务、商业模式等\u201c微观\u201d层面的应用，通过案例教学帮助学生理解可持续设计的实践路径。",
        "description_en": "A specialized course for graduate students that centers on the application of sustainable development theories and methods at the 'micro-level', including materials, products, services, and business models, helping students understand practical approaches to sustainable design through case studies."
    }
]

# ─── EUN JI CHO ───
ej = by_id['eun-ji-cho']
ej['bio_zh'] = "同济大学设计创意学院助理研究员，教授服务设计与社会创新设计课程，并担任与KISD（科隆国际设计学校）双学位项目的学术协调人。毕业于意大利米兰理工大学设计博士，荷兰代尔夫特理工大学交互设计硕士。在加入同济大学之前，曾在湖南大学担任助理教授。主要研究领域为面向社会创新的服务设计，特别关注社会可持续性与服务共创。自2010年起成为DESIS网络（社会创新与可持续设计网络）成员，并于2010至2013年在DESIS国际协调团队工作。她翻译了Ezio Manzini的著作《Design, When Everybody Designs: An Introduction to Design for Social Innovation》（MIT Press, 2015）的韩文版。"
ej['achievements'] = [
    {
        "name_zh": "Beyond Closed Doors：从独白到对话\u2014\u2014关注蛰居青年",
        "name_en": "Beyond Closed Doors: From Monologues to Dialogues with the Hikikomori",
        "description_zh": "在第11届韩国光州设计双年展上展出的社会创新设计研究项目，旨在调查韩国社会普遍存在的\u201c蛰居青年\u201d（hikikomori）现象。项目通过深度访谈收集了在社会竞争日益加剧的环境中选择退缩到自我空间的青年人的故事。这些故事被加工为微型叙事格式，在社交媒体上分享，同时也作为蛰居青年群体在线上进行开放、匿名的互动与连接的空间。项目通过设计介入探索社会包容与心理健康的新路径。",
        "description_en": "Featured at the 11th Gwangju Design Biennale in Korea, the project was initiated as a design research project aiming to investigate the phenomenon of socially withdrawn youth, often referred to as 'hikikomori'. Through in-depth interviews, the project collected the stories of socially withdrawn individuals who chose to retreat into their rooms after facing repeated failures and frustration in an increasingly competitive society. These stories, crafted into micro-storytelling formats, are shared on social media, also serving as an online space for open, anonymous interaction and connection among them."
    },
    {
        "name_zh": "7 Scenarios for Neighborhood of Care\u2014\u2014关怀邻里的七个场景展览",
        "name_en": "7 Scenarios for Neighborhood of Care Exhibition",
        "description_zh": "2021年12月10日至20日在上海四平街道富鑫社区中心举办的展览，展示了D&I研究生通过\u201cPSSD方法论与工具\u201d课程开发的7个服务设计概念，旨在更好地关爱四平社区中的弱势群体，包括老年人和精神障碍人士。社区居民，特别是富鑫社区中心的主要目标用户，参与了展览并使用展览中提供的反馈卡对服务概念提出了意见。展览促进了设计概念与社区居民之间的直接对话。",
        "description_en": "The exhibition \u2014 held at the Fuxin neighborhood community center from December 10 to 20, 2021 \u2014 shared 7 service concepts, developed by D&I postgraduate students through the course 'PSSD methodologies and tools', to better take care of vulnerable groups in the Siping neighborhood ranging from the elderly to the mentally challenged. Local residents, especially users of the Fuxin neighborhood community center, who are the main target users of many of the proposed services, joined the exhibition and shared their opinions on the service concepts by using feedback cards provided at the exhibition."
    }
]
ej['courses'] = [
    {
        "name_zh": "服务设计：方法与工具",
        "name_en": "Service Design: Methods and Tools",
        "description_zh": "注重动手实践的课程，旨在训练学生掌握核心服务设计工具，涵盖从用户理解工具（如人物画像、旅程地图）到系统分析（如系统地图）和概念呈现（如场景描述、服务蓝图）的全流程方法论。",
        "description_en": "Designed for hands-on learning, the course aims to train students to master essential service design tools, ranging from user-understanding tools (e.g., personas, journey maps) to system analysis (e.g., system maps) and concept presentations (e.g., scenarios, service blueprints)."
    }
]

# ─── TAO SIMIN ───
ts = by_id['tao-simin']
ts['achievements'] = [
    {
        "name_zh": "《热力学视角下气候建筑原型方法研究》专著",
        "name_en": "Research on the Prototype Method of Climatic Architecture from a Thermodynamic Perspective (Book)",
        "description_zh": "个人专著，中国社会科学出版社出版，国家社科基金后资助项目成果。本书探讨了在全球气候变化和能源问题日益突出的背景下，建筑如何以本体设计方式应对外部气候环境的问题，并提出\u201c气候建筑\u201d的概念，即以气候条件为出发点，通过改善室内热舒适和降低能耗来适应并利用外部环境的建筑。将建筑与其气候环境视为一个热力学开放系统，分析其能量流动方式并提出建筑气候策略的形式原型，建构了气候、能量、建筑和人之间的内在联系，明确了热力学视角下气候建筑原型研究的目标和意义。通过对传统民居案例的文献研究和实地调研，提取了气候建筑的\u201c结构\u2014层级\u2014因子\u201d形态梯度模型，并应用于当代气候建筑的设计实践，最终探讨了热力学原型在设计实践中的应用策略。",
        "description_en": "Her book, Research on the Prototype Method of Climatic Architecture from a Thermodynamic Perspective, was published by China Social Sciences Press and is an outcome of a project funded by the National Social Science Fund of China Post-funded Program. Set against the backdrop of increasingly pressing global climate change and energy issues, the book explores how architecture can respond to external climatic environments through an ontological design approach. It proposes the concept of \"climatic architecture,\" referring to architecture that takes climatic conditions as its starting point and adapts to and utilizes the external environment by improving indoor thermal comfort and reducing energy consumption. The book regards architecture and its climatic environment as a thermodynamic open system, analyzes patterns of energy flow, and proposes formal prototypes of architectural climate strategies. In doing so, it constructs the intrinsic relationships among climate, energy, architecture, and people, and clarifies the objectives and significance of prototype research on climatic architecture from a thermodynamic perspective. Through literature review and field investigation of traditional dwelling cases, the book extracts a \"structure\u2013hierarchy\u2013factor\" morphological gradient model of climatic architecture, applies it to contemporary climatic architectural design practice, and ultimately discusses application strategies for thermodynamic prototypes in design practice."
    }
]
ts['courses'] = [
    {
        "name_zh": "专业设计3：环境作为系统",
        "name_en": "Studio 3: Environment as System",
        "description_zh": "本科生课程。聚焦环境设计中的生态系统议题，教学核心是与空间、环境、生态绩效以及其中的协作关系等相关的系统性设计训练。",
        "description_en": "Undergraduate course. This course focuses on ecosystem-related issues in environmental design. Its teaching core lies in systematic design training related to space, environment, ecological performance, and the collaborative relationships embedded within them."
    },
    {
        "name_zh": "设计数据分析基础",
        "name_en": "Fundamentals of Design Data Analysis",
        "description_zh": "研究生课程。建立数据驱动设计的基本认知，在此基础上分别展开定量数据分析与定性数据分析的学习，并强调两类分析方法在可持续设计中的整合应用，用于支持设计决策与研究论证。",
        "description_en": "Graduate course. This course builds a basic understanding of data-driven design. On this basis, it introduces quantitative and qualitative data analysis methods respectively, while emphasizing the integrated application of both approaches in sustainable design to support design decision-making and research argumentation."
    },
    {
        "name_zh": "声音设计",
        "name_en": "Sound Design",
        "description_zh": "本科生课程。以整合设计的方式处理听觉媒介，研究声音的算法生成和交互形式，学习如何通过设计声音来传达不同情感化信息。",
        "description_en": "Undergraduate course. This course approaches auditory media through integrated design. It explores algorithmic sound generation and interactive forms, and guides students in learning how to communicate different emotional messages through the design of sound."
    }
]

# Write output
output = 'window.__SITE_DATA__ = ' + json.dumps(data, ensure_ascii=False, indent=2) + ';\n'
with open(DATA_FILE, 'w', encoding='utf-8') as f:
    f.write(output)

print(f"Updated data.js with {len(data)} faculty members")
for d in data:
    ach_count = len(d.get('achievements', []))
    crs_count = len(d.get('courses', []))
    print(f"  {d['id']}: {ach_count} achievements, {crs_count} courses")

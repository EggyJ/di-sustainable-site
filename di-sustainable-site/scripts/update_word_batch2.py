#!/usr/bin/env python3
"""Update data.js with full text from 4 additional Word documents.
Uses \u201c and \u201d for Chinese curly quotes to avoid Write tool corruption.
"""
import json, os

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(SITE_DIR, 'data.js'), 'r', encoding='utf-8') as f:
    content = f.read()

eq_idx = content.index('=')
json_str = content[eq_idx+1:].strip().rstrip(';').strip()
data = json.loads(json_str)

def find_faculty(d, fid):
    for i, f in enumerate(d):
        if f['id'] == fid:
            return i, f
    return None, None

LQ = '\u201c'  # left Chinese curly quote
RQ = '\u201d'  # right Chinese curly quote
LBR = '\u300a' # left book title mark
RBR = '\u300b' # right book title mark

# ============================================================
# 1. Saverio Silli
# ============================================================
idx, f = find_faculty(data, 'saverio-silli')
if f:
    f['bio_en'] = (
        "Saverio Silli is a designer, educator, and maker working at the intersection of "
        "digital fabrication, sustainability, and design education. With a background in "
        "architecture and product design, he was among the initiators of the Italian maker "
        "movement, contributing to the launch of the first FabLabs in Rome and promoting "
        "open, accessible approaches to technology and innovation.\n\n"
        "Since 2016, he has been Vice-Director of FabLab Shanghai at Tongji University's "
        "College of Design and Innovation, where he teaches digital fabrication, physical "
        "computing, and prototyping. His work focuses on empowering students to develop "
        "hands-on solutions that combine creativity, low-cost technologies, and responsible "
        "design thinking.\n\n"
        "Through workshops, research, and interdisciplinary projects, Saverio explores how "
        "fabrication and prototyping can become tools for embodiment within more-than-human "
        "and life-centered design approaches. He is particularly interested in how making "
        "processes help students physically engage with ecological systems, non-human "
        "perspectives, and future scenarios through tangible experimentation. His practice "
        "combines digital fabrication, open-source technologies, and AI-assisted design to "
        "encourage critical thinking, collaborative learning, and new forms of sustainable "
        "interaction between humans, technology, and the environment.\n\n"
        "A graduate of Fab Academy, the digital fabrication program directed by Prof. Neil "
        "Gershenfeld at MIT's Center for Bits and Atoms, Saverio later became a global "
        "mentor within the international FabLab Network and has contributed to educational "
        "initiatives and creative communities worldwide."
    )

    f['achievements'] = [
        {
            "name_zh": "Whatchamacallit " + LQ + "方法论" + RQ + "——通过物理构思实现人与自然互动",
            "name_en": "Whatchamacallit -- Human-Nature Interaction through Physical Ideation",
            "description_zh": (
                "与 Francesca Valsecchi 教授在" + LQ + "城市自然与制造" + RQ + "工作室中共同开发 Whatchamacallit 方法论。"
                "该项目将" + LQ + "极速原型制作（very rapid prototyping）" + RQ + "和动手制造作为支持生态共情（ecological empathy）"
                "和超越人类中心设计的工具。学生创造了改变感知、增强感官、通过具身体验和感官体验探索与城市自然"
                "全新互动方式的实验性装置。该方法论在 IASDR 2021 会议上以图文论文形式发表："
                + LBR + "利用制造与创客方法论支持生态共情的发展" + RBR + "。"
            ),
            "description_en": (
                "Co-developed the Whatchamacallit methodology within the Urban Nature and Fabrication "
                "studio with Prof. Francesca Valsecchi. The project introduced \"very rapid prototyping\" "
                "and hands-on fabrication as tools to support ecological empathy and more-than-human "
                "design. Students created experimental devices that altered perception, augmented senses, "
                "and explored new ways of interacting with urban nature through embodied and sensory "
                "experiences. The methodology was presented at the IASDR 2021 Conference with a pictorial: "
                "Leveraging on Fabrication and Making Methodologies to Support the Development of "
                "Ecological Empathy."
            )
        },
        {
            "name_zh": "PCB for Designers——将电子技术融入生态设计教育",
            "name_en": "PCB for Designers -- Integrating Electronics into Ecological Design Education",
            "description_zh": (
                "开发并主持 PCB for Designers 工作室课程，将电子电路设计、嵌入式编程和数字制造整合到交互与"
                "生态设计教育中。通过动手和体验式学习方法论，学生设计并制造全功能的电子设备，探索人与自然互动、"
                "生态感知和超越人类中心主义的视角。该教育框架和研究成果在 Bhutan FAB23 会议上发表，论文题目为"
                + LBR + "在设计工作室中整合电子电路设计与制造" + RBR + "，并获得" + LQ + "最佳会议论文" + RQ + "奖。"
            ),
            "description_en": (
                "Developed and directed PCB for Designers, a studio course integrating electronic circuit "
                "design, embedded programming, and digital fabrication into interaction and ecological "
                "design education. Through hands-on and experiential learning methodologies, students "
                "designed and fabricated fully functional electronic devices exploring human-nature "
                "interaction, ecological sensing, and more-than-human perspectives. The educational "
                "framework and research outcomes were presented at the Bhutan FAB23 Conference in the "
                "paper Integrating Electronic Circuit Design and Fabrication in a Design Studio, which "
                "won the \"Best conference paper\" award."
            )
        }
    ]

    f['courses'] = [
        {
            "name_zh": "开源硬件与编程",
            "name_en": "Open-source Hardware and Programming",
            "description_zh": (
                "通过体验式学习引入开源电子、嵌入式编程和数字制造。学生设计和原型制作交互系统，"
                "同时批判性地探索技术、感知和物理计算在设计实践中的作用。"
            ),
            "description_en": (
                "Hands-on course introducing open-source electronics, embedded programming, and digital "
                "fabrication through experiential learning. Students design and prototype interactive "
                "systems while critically exploring the role of technology, sensing, and physical "
                "computing in design practice."
            )
        },
        {
            "name_zh": "PCB for Designers",
            "name_en": "PCB for Designers",
            "description_zh": (
                "工作室课程，将电子电路设计、PCB制造和嵌入式系统整合到交互与生态设计中。"
                "通过快速原型制作和动手实验，学生开发探索人与自然互动和超越人类中心视角的电子设备。"
            ),
            "description_en": (
                "Studio course integrating electronic circuit design, PCB fabrication, and embedded "
                "systems into interaction and ecological design. Through rapid prototyping and hands-on "
                "experimentation, students develop electronic devices exploring human-nature interaction "
                "and more-than-human perspectives."
            )
        },
        {
            "name_zh": "城市自然与制造",
            "name_en": "Urban Nature and Fabrication",
            "description_zh": (
                "跨学科工作室，通过制造、感官探索和物理构思探索生态共情和人与自然互动。"
                "学生使用创客方法论和快速原型制作研究超越人类中心的设计场景。"
            ),
            "description_en": (
                "Interdisciplinary studio exploring ecological empathy and human-nature interaction "
                "through fabrication, sensory exploration, and physical ideation. Students use making "
                "methodologies and rapid prototyping to investigate more-than-human design scenarios."
            )
        },
        {
            "name_zh": "How Things Are Made (HTAM)",
            "name_en": "How Things Are Made (HTAM)",
            "description_zh": (
                "跨学科课程，研究产品在本地化生产系统中是如何被设计、制造、装配和文档化的。"
                "借鉴MIT创客教育方法，结合讲座、制造工作坊和协作微挑战，聚焦数字制造、可修复性、"
                "开源方法和可持续分布式制造。"
            ),
            "description_en": (
                "Cross-disciplinary course investigating how products are designed, fabricated, assembled, "
                "and documented within localized production systems. Inspired by MIT's maker-based "
                "learning approaches, the course combines lectures, fabrication workshops, and "
                "collaborative micro-challenges focused on digital fabrication, repairability, "
                "open-source methods, and sustainable distributed manufacturing."
            )
        }
    ]
    print("Updated: saverio-silli")

# ============================================================
# 2. Jarmo Suominen
# ============================================================
idx, f = find_faculty(data, 'jarmo-suominen')
if f:
    f['bio_en'] = (
        "Jarmo Suominen is an architect, researcher, educator, and environmental design practitioner "
        "working at the intersection of architecture, service design, urban innovation, sustainability, "
        "and human-AI interaction. He is Professor of Environmental Design and Program Director of "
        "Advanced Environmental Design at Tongji University, Shanghai, and serves as Vice Dean of the "
        "Shanghai Institute of Innovation and Design. He is deputy director in the MIT Tongji City Science "
        "Lab.\n\n"
        "His work builds on more than twenty years of experience at Aalto University in Finland and "
        "research and collaboration experience with MIT. Across these contexts, he has developed and led "
        "projects related to learning environments, university-city interfaces, workplace transformation, "
        "urban innovation, and sustainable spatial ecosystems. His work emphasizes architecture not only "
        "as the design of buildings, but as the design of spatial conditions that enable activity, "
        "access, collaboration, and long-term value formation.\n\n"
        "His current research examines architectural relevance under changing conditions through the "
        "Space-Activity-Value framework. He is especially interested in sustainable spatial use, "
        "adaptive reuse, distributed spatial resources, campus and city ecosystems, hybrid creativity, "
        "and the role of AI and emerging technologies in making spatial and social relationships more "
        "visible."
    )
    f['bio_zh'] = (
        "Jarmo Suominen 是一位建筑师、研究者、教育者和环境设计实践者，工作领域涵盖建筑学、"
        "服务设计、城市创新、可持续发展和人机交互的交叉领域。他现任同济大学环境设计教授，"
        "担任高级环境设计项目主任，同时兼任上海创新设计研究院副院长，以及 MIT 同济城市科学实验室副主任。\n\n"
        "他在芬兰阿尔托大学拥有二十余年的教学与研究经验，并与MIT保持长期合作。在这些学术背景下，"
        "他主导和参与了多个与学习环境、大学与城市接口、工作场所转型、城市创新和可持续空间生态系统"
        "相关的项目。他的工作强调建筑不仅是建筑物的设计，更是对空间条件的系统设计——"
        "这些条件能够支撑活动、可达性、协作和长期的价值创造。\n\n"
        "他当前的研究通过" + LQ + "空间-活动-价值（Space-Activity-Value）" + RQ + "框架审视建筑在不断变化条件下的"
        "相关性。他特别关注可持续空间利用、适应性再利用、分布式空间资源、校园与城市生态系统、"
        "混合创造力，以及AI和新兴技术在使空间与社会关系更加可视化方面的作用。"
    )

    f['achievements'] = [
        {
            "name_zh": "School as a Service——教育空间服务化",
            "name_en": "Space as a Service - Education",
            "description_zh": (
                "School as a Service 探索如何通过共享空间资源而非传统学校建筑来创建学习环境。"
                "该概念与阿尔托大学校园和埃斯波市立学校需求相关，重新思考了学校、校园、城市和"
                "日常学习之间的关系。它展示了空间充足性、可达性和机构协作如何支持新型教育形式和"
                "现有空间资源的可持续利用。"
            ),
            "description_en": (
                "School as a Service explores how learning environments can be created through shared "
                "spatial resources rather than only through a conventional school building. Developed "
                "in relation to the Aalto University campus and municipal school needs in Espoo, the "
                "concept rethinks the relationship between school, campus, city, and everyday learning. "
                "It demonstrates how spatial sufficiency, access, and institutional collaboration can "
                "support new forms of education and sustainable use of existing spatial resources."
            )
        },
        {
            "name_zh": "Spacent——分布式工作空间平台",
            "name_en": "Space as a Service -- Value Creation",
            "description_zh": (
                "Spacent 代表了从固定办公空间向分布式工作场所获取模式的转变。该概念聚焦于如何通过"
                "灵活获取不同空间资源（用于专注、会议、协作、移动和混合工作）来支持工作。"
                "它连接了建筑学、服务逻辑和数字平台，展示了如何通过获取性、可用性和智能利用现有空间"
                "来创造空间价值。"
            ),
            "description_en": (
                "Spacent represents a shift from fixed office space toward a distributed workplace-access "
                "model. The concept focuses on how work can be supported through flexible access to "
                "different spatial resources for concentration, meetings, collaboration, mobility, and "
                "hybrid work. It connects architecture, service logic, and digital platforms, showing how "
                "spatial value can be created through access, availability, and the intelligent use of "
                "existing spaces."
            )
        },
        {
            "name_zh": "MIT 同济城市科学实验室",
            "name_en": "MIT Tongji City Science Lab / City Science Collaboration",
            "description_zh": (
                "Jarmo Suominen 担任同济大学 MIT Tongji 城市科学实验室副主任，基于与 MIT 约二十年"
                "的研究与合作经验。该实验室连接城市创新、环境设计、数字技术和可持续空间发展，为探索"
                "校园、城市、社区和机构如何作为空间资源、活动、服务和公共价值的互联系统而发展提供了平台。"
            ),
            "description_en": (
                "Jarmo Suominen is Deputy Director of the MIT Tongji City Science Lab at Tongji University, "
                "building on around two decades of research and collaboration experience with MIT. The work "
                "connects urban innovation, environmental design, digital technologies, and sustainable "
                "spatial development. It has provided a platform for exploring how campuses, cities, "
                "communities, and institutions can be developed as interconnected systems of spatial "
                "resources, activities, services, and public value."
            )
        }
    ]

    f['courses'] = [
        {
            "name_zh": "环境设计工作室1",
            "name_en": "Environmental Design -- Studio 1",
            "description_zh": (
                "本课程将环境设计作为一种关系型设计实践进行介绍。它探讨空间环境、活动、用户、机构和"
                "价值形成如何随时间互动。课程鼓励学生超越单体建筑来理解建筑学，聚焦空间配置、共享资源、"
                "可达性和可持续利用。"
            ),
            "description_en": (
                "This course introduces environmental design as a relational design practice. It examines "
                "how spatial environments, activities, users, institutions, and value formation interact "
                "over time. The course encourages students to understand architecture beyond individual "
                "buildings, focusing instead on spatial configurations, shared resources, access, and "
                "sustainable use."
            )
        },
        {
            "name_zh": "服务建筑与空间生态系统工作坊",
            "name_en": "Service Architecture and Spatial Ecosystems - Workshops",
            "description_zh": (
                "本课程探索建筑如何支持服务系统、活动平台和空间生态系统。学生研究建筑、校园、公共空间"
                "和数字系统如何协同支持不断演变的使用模式。课程将建筑思维与服务设计、城市创新和可持续性连接起来。"
            ),
            "description_en": (
                "The course explores how architecture can support service systems, activity platforms, and "
                "spatial ecosystems. Students study how buildings, campuses, public spaces, and digital "
                "systems can work together to support evolving patterns of use. The course connects "
                "architectural thinking with service design, urban innovation, and sustainability."
            )
        },
        {
            "name_zh": "混合创造力：人、AI与机器人交互工作坊",
            "name_en": "Hybrid Creativity: Human, AI, and Robotic Interaction - Workshops",
            "description_zh": (
                "本课程探讨人类、人工智能和机器人技术之间的创造性协作。聚焦基于提示词的图像生成、"
                "机器人绘画、社区参与，以及设计师或艺术家作为机器生成内容和人工制造内容的诠释者、"
                "策展人和连接者的角色转变。"
            ),
            "description_en": (
                "This course examines creative collaboration between humans, artificial intelligence, "
                "and robotic technologies. It focuses on prompt-based image generation, robotic drawing, "
                "community participation, and the changing role of the designer or artist as interpreter, "
                "curator, and connector of machine-generated and human-made content."
            )
        }
    ]
    print("Updated: jarmo-suominen")

# ============================================================
# 3. Francesca Valsecchi
# ============================================================
idx, f = find_faculty(data, 'francesca-valsecchi')
if f:
    f['bio_en'] = (
        "Francesca Valsecchi (PhD) is Associate Professor at College of Design and Innovation, "
        "Tongji University.\n\n"
        "From participatory design research to immersive artistic practice, the work of Associate "
        "Professor Francesca Valsecchi looks at developing the \"green sense\" as the next liminal "
        "space of human perception and cognition. She works in Shanghai at Tongji University, "
        "College of Design and Innovation. She established the Ecology and Cultures Innovation Lab "
        "to discuss and experiment on more-than-human design and the challenges of post-development "
        "paradigms.\n\n"
        "Researches include published, speculative and exhibition works about mapping ecosystems, "
        "ethnography of waterscapes, ecological data, and urban-nature interaction, and social "
        "design. She is Italian, but she has been in Asia for more than a decade. Her teaching and "
        "research projects cover the areas of Design and Nature, Rural-Urban Innovation, Sustainable "
        "Food Systems, and more recently in the direction of Design for Ecosystems. She is an expert "
        "in creativity and visualization methods and participatory techniques, which she applied "
        "largely in artistic and research projects involving citizens and communities.\n\n"
        "She has an ongoing artistic practice using alternative photographic processes and bio-media. "
        "She is an environmental activist."
    )

    f['bio_zh'] = (
        "魏佛兰 博士，现任同济大学设计创意学院副教授。\n\n"
        "从参与式设计研究到沉浸式艺术实践，魏佛兰副教授的工作致力于探索" + LQ + "绿色感知（green sense）"
        "作为人类感知与认知下一种临界空间的发展方向。她现于上海同济大学设计创意学院开展教学与研究工作，"
        "并创立了" + LQ + "生态与文化创新实验室（Ecology and Cultures Innovation Lab）" + RQ + "，以讨论和实验"
        "" + LQ + "超越人类中心（more-than-human）" + RQ + "的设计方法，以及后发展（post-development）范式所面临的挑战。\n\n"
        "她的研究涵盖已发表研究、思辨设计（speculative design）及展览实践，主题包括生态系统制图、"
        "水域景观民族志、生态数据、城市与自然互动，以及社会设计等。她来自意大利，但已在亚洲生活和"
        "工作超过十年。她的教学与研究项目涉及" + LQ + "设计与自然" + RQ + "" + LQ + "城乡创新" + RQ + "" + LQ + "可持续食物系统" + RQ + "，以及"
        "近年来进一步拓展的" + LQ + "生态系统设计（Design for Ecosystems）" + RQ + "方向。她在创造力方法、可视化方法"
        "以及参与式技术方面具有丰富经验，并广泛应用于涉及公众与社区的艺术及研究项目中。\n\n"
        "同时，她持续进行以替代摄影工艺（alternative photographic processes）与生物媒介（bio-media）"
        "为核心的艺术实践，并积极参与环境行动主义。"
    )

    f['achievements'] = [
        {
            "name_zh": "海岸诗学：海岸共创艺术驻留计划",
            "name_en": "Poetry of the Coasts: Coastal Co-Art Residency",
            "description_zh": (
                "海岸生态系统是由潮汐、泥沙流动、盐度梯度、迁徙物种以及人类适应行为共同塑造的动态系统。"
                "这些变化不仅仅是科学意义上的描述，更是塑造生计方式、社会想象与政治叙事的文化力量。"
                "" + LQ + "海岸诗学（Poetry of the Coasts）" + RQ + "是一项为期一年的项目，由英国文化协会（British Council）"
                "资助，并得到同济大学与兰卡斯特大学支持。项目通过在中国崇明岛与英国莫克姆湾（Morecambe Bay）"
                "开展相互关联的艺术家驻留，发展一系列使跨尺度纠缠关系可视化的创作实践——从潮间带生命的"
                "微观场域，到海堤、排水渠道以及围垦边界等宏观基础设施。\n\n"
                "该项目结合生态艺术、参与式设计、环境人文学以及田野观察等跨学科方法。艺术家与研究者"
                "通过具身化场地探索、生态聆听、感官地图绘制、材料实验以及社区叙事等方式展开合作。"
                "科学知识与艺术诠释及地方经验形成对话，从而在英国与中国之间生成新的跨文化生态学习模式。"
            ),
            "description_en": (
                "Coastal ecologies are systems of motion shaped by tides, sediment flows, salinity "
                "gradients, migratory species, and human adaptation. These dynamics are not merely "
                "scientific descriptors but cultural forces shaping livelihoods, imaginaries, and "
                "political narratives. The Poetry of the Coasts is a year long project funded by "
                "British Council and supported by Tongji and Lancaster University that develop "
                "intertwined artists residency in the coastal environment of Chongming Island (China) "
                "and Morecambe Bay (UK) to develop projects that make visible the entanglement and "
                "relationships across scales, from microsites of tidal life to macro-infrastructures "
                "like seawalls, drainage channels, and land reclamation boundaries.\n\n"
                "The project combines transdisciplinary methods from ecological art, participatory "
                "design, environmental humanities, and field-based observation. Artists and researchers "
                "engage in embodied site explorations, ecological listening, sensory mapping, material "
                "experimentation, and community storytelling. Scientific knowledge is placed in dialogue "
                "with artistic interpretation and situated local experience, generating new forms of "
                "intercultural ecological learning between the UK and China."
            )
        },
        {
            "name_zh": "黄龙声景生态解说步道",
            "name_en": "Huanglong Acoustic Ecology Interpretation Trail",
            "description_zh": (
                "" + LQ + "黄龙声景生态解说步道" + RQ + "项目由同济大学设计创意学院与建筑与城市规划学院（CAUP）合作开展，"
                "位于中国四川黄龙景区（联合国教科文组织世界遗产地）。项目回应了传统自然展览与生态体验中的"
                "一个核心问题：对于非专业公众而言，生物多样性往往是" + LQ + "不可见" + RQ + "且" + LQ + "不可听" + RQ + "的。\n\n"
                "基于长达三年的生物声学监测研究，项目将原始生态数据转化为一种沉浸式、场地特定的学习系统。"
                "通过沿着一条220米高架步道设置的八个生态解说节点，声音互动被直接嵌入景观环境之中。"
                "每个节点都使访客能够主动参与鸟类声景的感知：借助定向聆听装置与同步视觉提示，"
                "使用者可以对超过60种鸟类的声音进行分离、比较与空间定位。\n\n"
                "这种方式使公众能够实时感知生态系统的复杂性，弥合科学监测与具身体验之间的距离。"
                "项目建立了一种将生物声学数据应用于空间解说与生态传播的新模式，以增强公众对于"
                "地方生态系统的理解与认知。"
            ),
            "description_en": (
                "In collaboration with CAUP (College of Architecture and Urban Planning), Huanglong "
                "Acoustic Ecology Interpretation Trail (in Huanglong Park, UNESCO World Heritage, "
                "Sichuan, China) addresses a key limitation of conventional nature exhibition and "
                "experiences: biodiversity is largely invisible and inaudible to non-experts.\n\n"
                "Based on three years of bio-acoustic monitoring, the project transforms raw ecological "
                "data into an immersive, site-specific learning system. It embeds sound-based "
                "interaction directly into the landscape through a sequence of eight interpretative "
                "nodes along a 220-metre elevated boardwalk. Each node enables visitors to actively "
                "engage with bird soundscapes: through directional listening interfaces and "
                "synchronised visual cues, it offers the possibility of isolating, comparing, and "
                "spatially locating more than 60 species. This allows users to perceive ecological "
                "complexity in real time, bridging the gap between scientific monitoring and embodied "
                "experience. The project establishes a new model for the application of bio-acoustic "
                "datasets in spatial interpretation and communication to strengthen public "
                "understanding of local ecology."
            )
        }
    ]

    f['courses'] = [
        {
            "name_zh": "Studio 1——生态复杂性叙事的传播与媒介工具",
            "name_en": "Studio 1 - Communication and Media Tools for the Narrative of Ecological Complexity",
            "description_zh": (
                "上海是一座由水塑造的超级城市，但其广阔的海岸边缘地带，对于大多数居民而言，"
                "依然是陌生且缺乏理解的空间。本工作室将海岸视为上海叙事中的核心角色，而非城市边缘。"
                "海岸并不是一条简单的边界线，而是一种" + LQ + "区域（zone）" + RQ + "——一个汇聚生态复杂性、物流强度、"
                "文化记忆与未来不确定性的场域。\n\n"
                "我们的任务是成为这一临界空间（liminal space）的" + LQ + "制图者（cartographers）" + RQ + "，"
                "通过设计研究去绘制其可见与不可见的多重层次。工作室将构建一个丰富的"
                "" + LQ + "挑衅性提案与研究物件（Provocations & Artefacts）" + RQ + "资料库，作为驻留艺术家的核心"
                "研究素材。学生的工作并非最终设计产品，而是一种" + LQ + "催化剂（catalyst）" + RQ + "——"
                "为艺术家建立一个可被进入、回应与再创造的世界。"
            ),
            "description_en": (
                "Shanghai is a megacity defined by its relationship with water, yet its vast coastal "
                "edges remain largely unknown or misunderstood by its inhabitants. This studio "
                "interprets the coast not as a periphery, but as a central character in the story of "
                "Shanghai. Coasts are zones, more than lines; sites of ecological complexity, "
                "logistical intensity, cultural memory, and future uncertainty. Our mission is to "
                "become cartographers of this liminal space, using design research to map its visible "
                "and invisible layers.\n\n"
                "The studio aims to produce a rich repository of \"Provocations & Artefacts\" that "
                "will serve as the primary research material for artists-in-residence. Your work is "
                "not a design product, but a catalyst. You are building the world that the artists "
                "will then inhabit and respond to."
            )
        },
        {
            "name_zh": "数据可视化——城市生态的数据结构与叙事",
            "name_en": "Data Visualisation - Visual Structures & Data Stories of Urban Ecology",
            "description_zh": (
                "本课程是一个聚焦数据可视化的强化教学模块，自2014年开设以来，旨在培养学生贯穿整个数据"
                "科学流程的设计能力——从数据采集到可视化制作，并建立对社会-技术数据景观（socio-technical "
                "datascapes）的批判性理解。\n\n"
                "面对快速变化的技术环境与能力需求，2026版课程尝试通过人工智能增强实践（AI-augmented "
                "practices）、工具基准比较（tool benchmarking）以及批判性视觉分析，重新定义数据可视化领域。"
                "课程不再仅仅关注线性的" + LQ + "数据处理管线（data pipelines）" + RQ + "，而是将可视化视为一种比较性的"
                "设计实践，以及一种研究与探究的方法。\n\n"
                "课程将数据可视化置于双重维度中讨论：作为一种研究方法（research methodology），支持探索、"
                "假设生成与分析性推理；作为一种公共传播媒介（public communication artefact），"
                "塑造叙事、感知与决策过程。"
            ),
            "description_en": (
                "This course is an intensive module in data visualisation, launched in 2014 to develop "
                "design skills that enable interaction with the whole process of data science, from "
                "data gathering to the craft of visualisations, and grounded in a critical outlook on "
                "socio-technical datascapes.\n\n"
                "Adapting to the fast-changing landscape of competencies and technologies, this 2026 "
                "edition of the course experiments with reframing the field through the lens of "
                "AI-augmented practices, tool benchmarking, and critical visual analysis. Rather than "
                "focusing solely on linear data pipelines, the course positions visualisation as both "
                "a comparative design practice and a method for inquiry.\n\n"
                "The module explores the role of communication design within contemporary data "
                "ecosystems, with particular attention to how AI-driven tools reshape the production, "
                "interpretation, and circulation of visualisations. Visualisation is addressed in its "
                "dual capacity: as a research methodology, supporting exploration, hypothesis "
                "generation, and analytical reasoning; and as a public communication artefact, shaping "
                "narratives, perception, and decision-making."
            )
        },
        {
            "name_zh": "Studio 5——城市自然",
            "name_en": "Studio 5 - Urban Nature",
            "description_zh": (
                "设计能够提升城市居民生态素养的人工物（artefacts），并使其作为城市生态景观中的"
                "" + LQ + "生态可供性（ecological affordances）" + RQ + "发挥作用。"
            ),
            "description_en": (
                "Designing artefacts that support ecological literacy among city dwellers and function "
                "as ecological affordances in the Urban Ecology landscape."
            )
        },
        {
            "name_zh": "Studio 5——感知生态",
            "name_en": "Studio 5 - Sensing Ecology",
            "description_zh": (
                "以生态代谢系统中的输入-输出机制为灵感，开展PCB电路设计与编程基础课程。"
            ),
            "description_en": (
                "Foundational course of PCB design and programming taking inspiration from input-output "
                "mechanism of ecological metabolic system."
            )
        }
    ]
    print("Updated: francesca-valsecchi")

# ============================================================
# 4. Wang Zisong
# ============================================================
idx, f = find_faculty(data, 'wang-zisong')
if f:
    f['name_zh'] = "汪滋淞"

    f['bio_zh'] = (
        "汪滋淞，副教授、博士生导师，长期以来从事可持续低碳设计，在绿色校园、生态城市规划、"
        "滨水城市设计、绿色建筑设计等方面开展研究及实践工作，并取得相关成果。主持及参与多项"
        "国家级、省部级、中央高校等科研项目。目前为中国城市科学研究会绿色建筑与节能专业委员会委员，"
        "中国城科会绿色建筑与节能专业委员会绿色校园学组秘书长，中国建筑节能协会南方中心委员、"
        "同济大学绿色建筑协会理事、国际绿色校园联盟委员等。\n\n"
        "作为第三编写人参与行业及国家标准" + LBR + "绿色校园评价标准" + RBR + "GB/T51356-2019编制，参编中国首部"
        "" + LQ + "中国绿色校园及绿色建筑节能知识" + RQ + "小学至大学5本系列教材，参编著作及教材十余本。作为指导老师"
        "指导学生多次获国际城市设计及景观设计大赛多个奖项，长期以来作为项目负责人完成绿色校园、"
        "城市规划、滨水城市设计、体育建筑等诸多项目，获得国家绿色建筑二星设计标识及运行标识多项。"
    )

    f['bio_en'] = (
        "Wang Zisong is Associate Professor and PhD Supervisor at Tongji University. He has long "
        "been engaged in sustainable low-carbon design, conducting research and practice in green "
        "campus, ecological urban planning, waterfront urban design, and green building design. "
        "He has presided over and participated in multiple national, provincial, and ministerial "
        "research projects.\n\n"
        "He serves as a committee member of the Green Building and Energy Conservation Committee of "
        "the China Association of City Science, Secretary-General of the Green Campus Sub-committee, "
        "committee member of the Southern Center of the China Building Energy Conservation Association, "
        "board member of the Tongji University Green Building Association, and committee member of "
        "the International Green Campus Alliance.\n\n"
        "As the third drafter, he participated in the compilation of the national standard \"Evaluation "
        "Standard for Green Campus\" GB/T 51356-2019. He also co-edited China's first series of textbooks "
        "on green campus and green building energy conservation knowledge covering primary school "
        "through university (5 volumes). He has guided students to win multiple awards in international "
        "urban design and landscape design competitions. As project lead, he has completed numerous "
        "projects in green campus, urban planning, waterfront urban design, and sports architecture, "
        "obtaining multiple National Green Building Two-Star Design and Operation certifications."
    )

    f['achievements'] = [
        {
            "name_zh": LBR + "绿色校园评价标准" + RBR + " GB/T51356-2019 国家标准编制",
            "name_en": "National Standard: Evaluation Standard for Green Campus GB/T 51356-2019",
            "description_zh": (
                "汪滋淞副教授作为国家标准" + LBR + "绿色校园评价标准" + RBR + " GB/T 51356-2019的位列第三位的主要编写人，"
                "该标准涵盖中小学、职业学校、高校绿色校园建设评估内容，作为评估中国的绿色校园建设标准。"
                "标准于2019年10月1日实施。同时作为行业标准" + LBR + "绿色校园评价标准" + RBR + " CSUS/GBC 04-2013列第三"
                "编写人及标准协调人，标准2013中国绿色校园建设标准，2013年4月1日实施，该标准涵盖中小学及"
                "高校绿色校园建设内容作为评估依据。"
            ),
            "description_en": (
                "As the third principal drafter of the national standard \"Evaluation Standard for "
                "Green Campus\" GB/T 51356-2019, Wang Zisong contributed to a comprehensive framework "
                "covering primary schools, vocational schools, and universities for green campus "
                "assessment. The standard was implemented on October 1, 2019. He also served as the "
                "third drafter and coordinator of the industry standard CSUS/GBC 04-2013, implemented "
                "on April 1, 2013."
            )
        },
        {
            "name_zh": LBR + "绿色校园与未来" + RBR + "系列教材参编",
            "name_en": "Green Campus and Future Textbook Series",
            "description_zh": (
                LBR + "绿色校园与未来" + RBR + "（1-5册），中国首部" + LQ + "中国绿色校园及绿色建筑节能知识" + RQ + "小学至大学"
                "5本系列教材。该教材是我国首部一套贯穿基础教育到高等教育的系列教材，由吴志强院士为主编，"
                "汪滋淞副教授参编，会同国内外多个知名大中小学校长、一线教师与绿色建筑专家共同编制，"
                "针对不同学段的知识结构和教学特点设置基准主题，通过全学段知识点的层层递进辅以经典案例"
                "和主题活动，培养学生绿色可持续发展的核心价值观、绿色生态知识体系的建构以及绿色生活"
                "习惯的养成。2015年由中国建筑工业出版社正式出版，并已在上海等地开办示范课程。"
            ),
            "description_en": (
                "\"Green Campus and Future\" (Volumes 1-5) is China's first textbook series on green "
                "campus and green building energy conservation knowledge, covering primary school "
                "through university. Edited by Academician Wu Zhiqiang with co-editor Wang Zisong, "
                "the series was jointly compiled by renowned school principals, frontline teachers, "
                "and green building experts. It establishes progressively layered knowledge points "
                "across all educational stages, supplemented by classic cases and thematic activities, "
                "to cultivate students' core values of green sustainable development, green ecological "
                "knowledge systems, and green living habits. Published by China Architecture & "
                "Building Press in 2015, with demonstration courses launched in Shanghai and other cities."
            )
        },
        {
            "name_zh": "无锡市五爱小学雪枫分校设计",
            "name_en": "Wuxi Wuai Primary School Xuefen Branch Campus Design",
            "description_zh": (
                "汪滋淞副教授2021年主持设计的无锡市五爱小学雪枫分校（已建成）获第十六届园冶杯国际竞赛"
                "国际建筑奖金奖，并获国家二星绿色建筑认证。无锡市五爱小学雪枫分校位于无锡市梁溪区北滨路"
                "北侧、全丰路西侧，学校用地面积约33342平方米的36班制小学，建筑面积约为33272平方米，"
                "配置各配套功能用房，包括教学用房、专用教室、图书阅览、行政用房、风雨操场、食堂、"
                "运动场地及其他附属设施等。"
            ),
            "description_en": (
                "The Wuxi Wuai Primary School Xuefen Branch Campus, designed by Wang Zisong in 2021 "
                "(completed), won the Gold Award in the International Architecture category at the 16th "
                "Yuanye Cup International Competition and received the National Two-Star Green Building "
                "Certification. Located on Beibin Road, Liangxi District, Wuxi, the 36-class primary "
                "school covers approximately 33,342 square meters with a building area of approximately "
                "33,272 square meters, including teaching rooms, specialized classrooms, library, "
                "administrative offices, indoor gymnasium, cafeteria, sports grounds, and other "
                "supporting facilities."
            )
        }
    ]

    f['courses'] = [
        {
            "name_zh": "设计技术1（本科）",
            "name_en": "Design Technology 1 (Undergraduate)",
            "description_zh": (
                "从空间的形成与组织、空间形态和结构、空间的材料组织等角度出发，帮助学生深刻理解"
                "" + LQ + "可持续设计" + RQ + "的设计理念并了解如何应用在设计中。可持续设计是对人与环境关系的主动构建。"
                "课程引导学生在空间组织、自然要素利用与行为引导中，回应生态规律，创造低负担、高适应的"
                "人居环境，使设计兼具环境效益、使用价值与社会公平。"
            ),
            "description_en": (
                "From the formation and organization of space, spatial morphology and structure, and "
                "material organization of space, the course helps students deeply understand the design "
                "philosophy of \"sustainable design\" and learn how to apply it. Sustainable design is "
                "an active construction of the relationship between humans and the environment. The "
                "course guides students to respond to ecological principles in spatial organization, "
                "natural element utilization, and behavioral guidance, creating low-burden, highly "
                "adaptive human settlements that combine environmental benefits, use value, and social equity."
            )
        },
        {
            "name_zh": "设计实践研究专题2——协同设计（硕士）",
            "name_en": "Design Practice Research Seminar 2 - Collaborative Design (Postgraduate)",
            "description_zh": (
                "围绕博物馆、科技馆展陈更新改造的可持续转型与科技转型，将可持续设计与交互设计深度融合。"
                "学生依托可持续设计、虚拟现实、智能交互等技术，设计高适配、低更新负荷的交互叙事与空间环境。"
                "设计内容包括上海科技馆的自然馆的碳足迹展示设计、材料馆的可持续设计相关内容。课程关注"
                "如何通过实时反馈的科技馆交互系统引导观众形成低碳认知与行为习惯，让每一次参观都成为"
                "一种促进人与环境良性互动的可持续设计实践。"
            ),
            "description_en": (
                "Focusing on the sustainable transformation and technological transition of museum and "
                "science museum exhibition renovations, this course deeply integrates sustainable design "
                "with interaction design. Students leverage sustainable design, virtual reality, and "
                "intelligent interaction technologies to design highly adaptive, low-maintenance "
                "interactive narratives and spatial environments. Projects include carbon footprint "
                "display design for the Nature Hall and sustainable design content for the Materials "
                "Hall at the Shanghai Science and Technology Museum. The course explores how real-time "
                "feedback interactive systems can guide visitors toward low-carbon awareness and behavioral "
                "habits, making every visit a sustainable design practice that promotes positive "
                "human-environment interactions."
            )
        }
    ]
    print("Updated: wang-zisong")

# Write updated data.js
json_output = json.dumps(data, ensure_ascii=False, indent=2)
with open(os.path.join(SITE_DIR, 'data.js'), 'w', encoding='utf-8') as f:
    f.write('window.__SITE_DATA__ = ')
    f.write(json_output)
    f.write(';\n')

with open(os.path.join(SITE_DIR, 'faculty.json'), 'w', encoding='utf-8') as f:
    f.write(json_output)

print("\nDone! data.js and faculty.json updated.")

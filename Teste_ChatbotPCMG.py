{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPzKAFE45tZHY3+cnhQaxry",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/diegomicael/Imersao-IA-Alura/blob/main/Teste_ChatbotPCMG.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -q -U google-generativeai"
      ],
      "metadata": {
        "id": "MQJn6nc7fxrj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "BGNykV7YsXIe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Import the Python SDK\n",
        "import google.generativeai as genai\n",
        "from google.colab import userdata\n",
        "api_key = userdata.get('SECRET_KEY')\n",
        "genai.configure(api_key=api_key)"
      ],
      "metadata": {
        "id": "U5pRufTYituB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for m in genai.list_models():\n",
        "  if 'generateContent' in m.supported_generation_methods:\n",
        "   print(m.name)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 145
        },
        "id": "TDuMujyai_DS",
        "outputId": "fe1905c3-15cc-48e5-c0f9-f6a1cdc28b4c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "models/gemini-1.0-pro\n",
            "models/gemini-1.0-pro-001\n",
            "models/gemini-1.0-pro-latest\n",
            "models/gemini-1.0-pro-vision-latest\n",
            "models/gemini-1.5-pro-latest\n",
            "models/gemini-pro\n",
            "models/gemini-pro-vision\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "generation_config = {\n",
        "    \"candidate_count\": 1,\n",
        "    \"temperature\" : 0.5,\n",
        "    \"top_p\" : 0.5,\n",
        "    \"top_k\" : 0.5,\n",
        "\n",
        "}"
      ],
      "metadata": {
        "id": "CA1-ohvilHbt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "safety_settings = {\n",
        "    \"Harassment\": \"BLOCK_NONE\",\n",
        "    \"Hate\": \"BLOCK_NONE\",\n",
        "    \"Sexual\": \"BLOCK_NONE\",\n",
        "    \"Dangerous\": \"BLOCK_NONE\",\n",
        "    }"
      ],
      "metadata": {
        "id": "DJZCNs_dmxfU"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model = genai.GenerativeModel(model_name=\"gemini-1.0-pro\",\n",
        "                              generation_config=generation_config,\n",
        "                              safety_settings=safety_settings)"
      ],
      "metadata": {
        "id": "h6_vsaBhom5c"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import time"
      ],
      "metadata": {
        "id": "j0Ic9N-H8hws"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "timer_start = time.time()  # Iniciar contagem ao iniciar o chatbot"
      ],
      "metadata": {
        "id": "1bgzIyWZ8i8Q"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from os import openpty\n",
        "\n",
        "def chatbot():\n",
        "  print(\"\"\"Olá!\n",
        "\n",
        "Este é o \"CONECTA PCMG\", canal de atendimento digital da 9ª Delegacia de Polícia Civil de Abaeté-MG\n",
        "Trata-se de um canal dedicado para envio de intimações, captação de arquivos, mídias e dados relacionadas a procedimentos.\n",
        "\n",
        "Digite o número correspondente ao setor ou informação desejada:\n",
        "\"\"\")\n",
        "\n",
        "  while True:\n",
        "    menu = \"\"\"\n",
        "    Menu:\n",
        "    1. Identidade\n",
        "    2. Registro de Ocorrência\n",
        "    3. Cópia de Ocorrência\n",
        "    4. Denúncias\n",
        "    5. Violência Doméstica / Medidas Protetivas\n",
        "    6. Intimações\n",
        "    7. Trânsito\n",
        "    8. Atestado de Antecedentes\n",
        "    9. Telefones úteis\n",
        "    0. Envio de Arquivos\n",
        "\n",
        "    Digitar - Para enviar uma mensagem\n",
        "    Menu - Para voltar ao Menu Principal\n",
        "    Sair - Encerrar atendimento\n",
        "    \"\"\"\n",
        "    print(menu)\n",
        "\n",
        "    opcao = input(\"Escolha uma opção: \")\n",
        "\n",
        "    if opcao == '1':\n",
        "      print(\"\"\"\n",
        "Como solicitar?\n",
        "\n",
        "Para solicitar a emissão da carteira de identidade, é necessário realizar o agendamento diretamente na Delegacia  de Polícia Civil de Abaeté, de Segunda à Sexta, das 08hs30min às 10hs30min e de 14hs às 15hs30min.\n",
        "\n",
        "Quais documentos levar?\n",
        "\n",
        "•Se solteiro, certidão de nascimento.\n",
        "•Se casado, certidão de casamento (obrigatoriamente caso o solicitante tenha alterado o nome em razão do casamento) ou certidão de nascimento com a averbação do casamento (se não houve alteração do nome em virtude do casamento).\n",
        "•Se divorciado, certidão de casamento com averbação do divórcio ou certidão de nascimento com averbação do divórcio.\n",
        "\n",
        "Documentos opcionais que podem ser incluídos no RG, mediante comprovação:\n",
        "\n",
        "•CPF\n",
        "•CNH\n",
        "•Titulo de Eleitoral\n",
        "•Carteira de Trabalho\n",
        "•Cartão do SUS\n",
        "•Certificado de Reservista\n",
        "•Carteira Profissional\n",
        "•Tipo Sanguíneo\n",
        "\n",
        "Importante:\n",
        "\n",
        "•A certidão apresentada deverá ser original.\n",
        "•A certidão deverá estar legível, sem rasgos, emendas ou rasuras que comprometam a originalidade do documento.\n",
        "•O menor de 16 anos deverá estar acompanhado pelo pai ou pela mãe, que deverá apresentar documento oficial com foto que o (a) identifique.\n",
        "\n",
        "Atenção:\n",
        "\n",
        "\n",
        "A PRIMEIRA VIA DA NOVA CARTEIRA É GRATUITA.\n",
        "\n",
        "\n",
        "•Não é mais necessário levar fotos 3x4. A fotografia será tirada no momento do atendimento - com exceção de crianças que não possam posar sem amparo de terceiros. Não é permitido tirar a fotografia usando qualquer espécie de cobertura de cabeça (lenço, chapéu, boné) nem com óculos de sol. Serão aceitas coberturas que compõem hábitos religiosos que façam parte do uso cotidiano do portador ou em razão de motivos de saúde.\n",
        "\n",
        "\n",
        "Esta é uma mensagem automática, dúvidas ligue (37) 3541-1489.\n",
        "No site oficial, a delegacia online oferece links para os serviços e também para outros recursos, como Polícia Civil e Detran MG.\n",
        "\n",
        "A Delegacia Virtual MG  também fornece para download guias com informações sobre o enfrentamento da violência doméstica e familiar contra a mulher.\n",
        "\n",
        "O objetivo da criação da Delegacia Virtual é a diminuição no tempo de espera em unidades policiais, além de combater a subnotificação de registros.\n",
        "https://delegaciavirtual.sids.mg.gov.br/\n",
        "\n",
        "Esta é uma mensagem automática, dúvidas ligue (37) 3541-1489.\n",
        "      \"\"\")\n",
        "\n",
        "    elif opcao == '2':\n",
        "      print(\"\"\"\n",
        "DELEGACIA VIRTUAL DO ESTADO DE MINAS GERAIS\n",
        "\n",
        "O serviço da Delegacia Virtual MG é mais uma maneira do cidadão fazer um registro de ocorrência, com o diferencial de fazer o procedimento por meio da internet.\n",
        "No site oficial, a delegacia online oferece links para os serviços e também para outros recursos, como Polícia Civil e Detran MG.\n",
        "\n",
        "A Delegacia Virtual MG  também fornece para download guias com informações sobre o enfrentamento da violência doméstica e familiar contra a mulher.\n",
        "O objetivo da criação da Delegacia Virtual é a diminuição no tempo de espera em unidades policiais, além de combater a subnotificação de registros.\n",
        "https://delegaciavirtual.sids.mg.gov.br/\n",
        "\n",
        "Esta é uma mensagem automática, dúvidas ligue (37) 3541-1489.\n",
        "      \"\"\")\n",
        "    elif opcao == '3':\n",
        "      print(\"\"\"\n",
        "CÓPIA DE OCORRÊNCIA\n",
        "\n",
        "Fornecimento de copia de ocorrência em arquivo digital, do Boletim de Ocorrência Policial (BO) poderá ser solicitado através do site https://cidadao.mg.gov.br/#/login?codRecurso=DELEGACIAVIRTUAL015\n",
        "\n",
        "QUEM PODE UTILIZAR O SERVIÇO?\n",
        "\n",
        "Qualquer cidadão que tenha registrado um Boletim de Ocorrência Policial (BO) ou ainda que não tenha solicitado o registro, conste como um dos envolvidos na ocorrência.\n",
        "\n",
        "RESTRIÇÕES\n",
        "\n",
        "Estão disponíveis para impressão os registros das seguintes naturezas:\n",
        "\n",
        "•\tAcidente de trânsito com vítima\n",
        "•\tAcidente de trânsito sem vítima\n",
        "•\tAmeaça\n",
        "•\tAplicação das medidas administrativas Código de Trânsito Brasileiro (CTB)\n",
        "•\tAtrito verbal\n",
        "•\tComunicação de pessoa extraviada ou desaparecida\n",
        "•\tDano\n",
        "•\tDescumprimento de medida protetiva de urgência\n",
        "•\tEstelionato\n",
        "•\tExtravio de documentos\n",
        "•\tExtravio de objetos pessoais\n",
        "•\tFurto\n",
        "•\tLesão corporal\n",
        "•\tOutras ações de defesa social\n",
        "•\tOutras infrações contra a pessoa\n",
        "•\tOutras infrações contra o patrimônio\n",
        "•\tOutras infrações demais leis especiais\n",
        "•\tPessoa localizada\n",
        "•\tRoubo\n",
        "•\tVeículo localizado/recuperado\n",
        "•\tVias de fato/agressão\n",
        "•\tExplosão e Incêndio\n",
        "•\tPrevenção e Vistoria\n",
        "•\tAtividades de proteção e Defesa Civil\n",
        "•\tBusca e salvamento\n",
        "•\tAtendimento Pré-hospitalar (APH)\n",
        "•\tDemonstrações, palestras e treinamentos\n",
        "•\tComunicações, denúncias, reclamações e solicitações diversas\n",
        "•\tCoordenação e controle operacional e administrativo\n",
        "•\tOperações de Defesa Social\n",
        "\n",
        "Caso tenha dificuldades em emitir o Boletim de Ocorrência Policial (BO) através do site, poderá encaminhar o número do registro que encaminharemos o arquivo assim que possível.\n",
        "\n",
        "Esta é uma mensagem automática, dúvidas ligue (37) 3541-1489.\n",
        "      \"\"\")\n",
        "    elif opcao == '4':\n",
        "      print(\"\"\"\n",
        "      DENÚNCIAS\n",
        "\n",
        "      Para denunciar, basta ligar, gratuitamente, para o número 181.\n",
        "      O Disque Denúncia funciona com uma central de atendimento unificada, formada por profissionais treinados e capacitados que trabalham em regime de 24 horas para atender à população.\n",
        "      Cada denúncia registrada é encaminhada para uma equipe de analistas composta por um integrante da Polícia Civil, da Polícia Militar e do Corpo de Bombeiros.\n",
        "\n",
        "Esta é uma mensagem automática, dúvidas ligue (37) 3541-1489.\"\"\")\n",
        "\n",
        "    elif opcao == '5':\n",
        "      print(\"\"\"\n",
        "      VIOLÊNCIA DOMÉSTICA / MEDIDAS PROTETIVAS\n",
        "\n",
        "O registro de ocorrência relacionado com violência contra a mulher pode ser feito:\n",
        "\n",
        "* Delegacia Especializada em Atendimento à Mulher\n",
        "* Em qualquer Delegacia de Polícia Civil de Minas Gerais\n",
        "* Pela Delegacia Virtual https://delegaciavirtual.sids.mg.gov.br Obs.: É possível registrar ocorrências de lesão corporal, vias de fato, ameaça e descumprimento de medida protetiva.\n",
        "* Em qualquer unidade da Polícia Militar de Minas Gerais (PMMG).\n",
        "\n",
        "Na delegacia, a mulher em situação de violência poderá:\n",
        "\n",
        "•\t Solicitar medidas protetivas de urgência.\n",
        "•\t Solicitar acompanhamento até o endereço informado para que ela possa retirar seus pertences em segurança (roupas, documentos e medicamentos).\n",
        "•\t Receber a guia de exame de corpo de delito.\n",
        "•\t Solicitar encaminhamento para casas abrigo.\n",
        "•\t Realizar a representação criminal para a devida responsabilização do agressor.\n",
        "•\t Ser encaminhada para serviços de atendimento psicossocial.\n",
        "•\t Ser incluída em programa de prevenção da Policia Militar.\n",
        "•\t Receber encaminhamento para orientação jurídica na Defensoria Pública.\n",
        "\n",
        "Representação Criminal:\n",
        "\n",
        "•Em alguns crimes, a investigação depende da representação da vítima.\n",
        "•Medidas protetivas podem ser solicitadas sem representação, mas não há investigação ou punição do agressor.\n",
        "•Em outros casos, a investigação ocorre independente da vontade da vítima, como em estupro, lesão corporal e tentativa de feminicídio.\n",
        "\n",
        "Medidas Protetivas:\n",
        "\n",
        "•Direitos previstos na Lei Maria da Penha para proteger mulheres em situação de violência.\n",
        "•Podem ser solicitadas em casos de violência física, psicológica, sexual, patrimonial ou moral.\n",
        "•Disponíveis para todas as mulheres, independente de orientação sexual, raça, etnia, etc.\n",
        "\n",
        "Solicitação de Medidas Protetivas:\n",
        "\n",
        "•Pode ser feita na Delegacia de Polícia, Ministério Público ou Defensoria Pública, sem advogado.\n",
        "•Um juiz analisará o pedido e decidirá sobre as medidas.\n",
        "•As medidas podem incluir: afastamento do agressor, proibição de contato, uso de tornozeleira eletrônica, etc.\n",
        "•As medidas são independentes do processo criminal e podem ser deferidas mesmo que não haja crime.\n",
        "\n",
        "\n",
        "Para mais informações baixe a cartilha da PCMG sobre Medida Protetiva através do link https://www.policiacivil.mg.gov.br/site-pc/media/get/documento/3845194 ou procure diretamente a Delegacia de Polícia Civil mais próxima.\n",
        "\n",
        "Esta é uma mensagem automática, dúvidas ligue (37) 3541-1489.\n",
        "      \"\"\")\n",
        "\n",
        "    elif opcao == '6':\n",
        "      print(\"\"\"\n",
        "      INTIMAÇÕES\n",
        "\n",
        "Para maiores informações, comparecer à Delegacia de Policia Civil de Abaeté, Rua Inácio de Oliveira Campos, nº 335, Bairro Amazonas, de posse do número do procedimento, das 8hs às 12hs e das 14hs às 18hs. Nenhuma informação com relação ao procedimento será repassada pelo telefone.\n",
        "      \"\"\")\n",
        "\n",
        "    elif opcao == '7':\n",
        "      print(\"\"\"\n",
        "      TRÂNSITO\n",
        "\n",
        "Serviços e informações oficiais sobre Veículos, Habilitação e Infrações, acesse o site do Departamento de Trânsito de Minas Gerais - Detran-MG.\n",
        "https://www.transito.mg.gov.br/ ou pessoalmente na unidade policial.\n",
        "\n",
        "Esta é uma mensagem automática, dúvidas ligue (37) 3541-1489.\n",
        "      \"\"\")\n",
        "\n",
        "    elif opcao == '8':\n",
        "      print(\"\"\"\n",
        "      ATESTADO DE ANTECEDENTES\n",
        "\n",
        "O atestado de antecedentes é um documento gratuito emitido pela Polícia Civil, por meio do Instituto de Identificação, que apresenta a existência ou não de antecedentes criminais do cidadão requisitante no exato momento da solicitação.\n",
        "\n",
        "Para os portadores de Carteira de Identidade do Estado de Minas Gerais, o serviço está disponível on line. O Atestado de Antecedentes para portadores de Carteira de Identidade de outros Estados deve ser requerido pessoalmente em uma Unidade Integrada de Atendimento (UAI). No interior do Estado de Minas, onde não houver atendimento nos Postos de Identificação, o interessado pode procurar uma Delegacia de Polícia Civil mais próxima.\n",
        "\n",
        "Menores de 18 anos não têm obrigação legal de apresentar Atestado de Antecedentes. Diante disso, o sistema não emite o documento. Cabe salientar que o não fornecimento do Atestado de Antecedentes não implica, necessariamente, a existência de pendências jurídico-criminais.\n",
        "\n",
        "https://wwws.pc.mg.gov.br/atestado\n",
        "\n",
        "Esta é uma mensagem automática, dúvidas ligue (37) 3541-1489.\n",
        "      \"\"\")\n",
        "\n",
        "    elif opcao == '9':\n",
        "      print(\"\"\"\n",
        "      TELEFONES ÚTEIS\n",
        "\n",
        "Policia Civil de Abaeté (37)3541-1489\n",
        "Polícia Militar (37)3541-1344\n",
        "Disque Denúncia 181\n",
        "Presídio (37)3541-1535\n",
        "UPA (37)3541-5377\n",
        "Promotoria (37)3541-1013\n",
        "Fórum (37)3541-1797\n",
        "Prefeitura (37)3541-5151\n",
        "Conselho Tutelar (37)3541-5044\n",
        "Clínica São José (37)3541-2272\"\"\")\n",
        "\n",
        "    elif opcao == '0':\n",
        "      print(\"\"\"\n",
        "      ENVIO DE ARQUIVOS\n",
        "\n",
        "      Ao encaminhar arquivos, fotos, áudios, prints, comprovantes e demais informações para instrução de procedimentos, favor constar os seguintes dados:\n",
        "\n",
        "Nome completo e RG;\n",
        "Numero da ocorrência ou do procedimento (caso saiba informar);\n",
        "Nome do servidor responsável pelo atendimento.\n",
        "\n",
        "Basta enviar os arquivos que estes serão incluídos nos respetivos procedimentos.\"\"\")\n",
        "      input(\"Digite sua mensagem: \")\n",
        "\n",
        "    elif opcao.lower() == 'menu':\n",
        "      continue  # Volta ao início do loop e mostra o menu\n",
        "    elif opcao.lower() == 'digitar':\n",
        "      input(\"Digite sua mensagem: \")\n",
        "    elif opcao.lower()== 'sair':\n",
        "      print(\"\"\"\n",
        "      Seu atendimento foi encerrado.\n",
        "      A 9ª Delegacia de Polícia Civil de Abaeté agradece o seu contato.\n",
        "      Caso ainda precise de nosso atendimento, digite: Menu\"\"\")\n",
        "\n",
        "      input(\"Digite sua mensagem: \")\n",
        "\n",
        "    elif opcao.lower() == 'Fim':\n",
        "      break  # Sai do loop e encerra o atendimento\n",
        "\n",
        "\n",
        "    else:\n",
        "      print(\"Opção inválida. Por favor, escolha uma opção do menu.\")\n",
        "\n",
        "  print(\"\"\"\n",
        "Seu atendimento foi encerrado.\n",
        "A 9ª Delegacia de Polícia Civil de Abaeté agradece o seu contato.\"\"\")\n",
        "\n",
        "\n",
        "\n",
        "chatbot()\n"
      ],
      "metadata": {
        "id": "SYT42qHHgjHq",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 772
        },
        "outputId": "ac494717-4048-4619-b6c3-e6f85255ad7a"
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Olá!\n",
            "\n",
            "Este é o \"CONECTA PCMG\", canal de atendimento digital da 9ª Delegacia de Polícia Civil de Abaeté-MG\n",
            "Trata-se de um canal dedicado para envio de intimações, captação de arquivos, mídias e dados relacionadas a procedimentos.\n",
            "\n",
            "Digite o número correspondente ao setor ou informação desejada:\n",
            "\n",
            "\n",
            "    Menu:\n",
            "    1. Identidade\n",
            "    2. Registro de Ocorrência\n",
            "    3. Cópia de Ocorrência\n",
            "    4. Denúncias\n",
            "    5. Violência Doméstica / Medidas Protetivas\n",
            "    6. Intimações\n",
            "    7. Trânsito\n",
            "    8. Atestado de Antecedentes\n",
            "    9. Telefones úteis\n",
            "    0. Envio de Arquivos\n",
            "\n",
            "    Digitar - Para enviar uma mensagem\n",
            "    Menu - Para voltar ao Menu Principal\n",
            "    Sair - Encerrar atendimento\n",
            "    \n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "Interrupted by user",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-1-472cd609c836>\u001b[0m in \u001b[0;36m<cell line: 287>\u001b[0;34m()\u001b[0m\n\u001b[1;32m    285\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    286\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 287\u001b[0;31m \u001b[0mchatbot\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m<ipython-input-1-472cd609c836>\u001b[0m in \u001b[0;36mchatbot\u001b[0;34m()\u001b[0m\n\u001b[1;32m     30\u001b[0m     \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmenu\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     31\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 32\u001b[0;31m     \u001b[0mopcao\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Escolha uma opção: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     33\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     34\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mopcao\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'1'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m    849\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    850\u001b[0m             )\n\u001b[0;32m--> 851\u001b[0;31m         return self._input_request(str(prompt),\n\u001b[0m\u001b[1;32m    852\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    853\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    893\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    894\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 895\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    896\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    897\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ]
    }
  ]
}
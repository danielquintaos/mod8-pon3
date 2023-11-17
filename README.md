Este pacote ROS (`my_ros_chatbot_package`) implementa um chatbot para interação com um robô de serviço, permitindo ao usuário enviar comandos intuitivos e diretos para o robô, como "Vá para a secretaria" ou "Leve-me à biblioteca".

## Instalação
Siga estas etapas para instalar o pacote:
1. **Clone o Repositório**:
   Clone este repositório no diretório `src` do seu workspace ROS.
   ```bash
   cd ~/seu_workspace_ros/src
   git clone https://github.com/danielquintaos/mod8-pon3
   ```
2. **Compile o Workspace**:
   Navegue de volta ao root do seu workspace ROS e compile.
   ```bash
   cd ..
   colcon build
   ```
3. **Source o Setup**:
   Source o arquivo de setup.
   ```bash
   source install/setup.bash # Para ROS 2
   ```

## Uso
Para iniciar o nó do chatbot, execute o comando abaixo:
```bash
roslaunch my_ros_chatbot_package chatbot_launch.launch
```

## Estrutura do Pacote
- `CMakeLists.txt` & `package.xml`: Arquivos essenciais para a construção e gestão de dependências.
- `scripts/`: Contém scripts Python executáveis, como o `chatbot_node.py`.
- `launch/`: Arquivos de lançamento do ROS.
- `config/`: Arquivos de configuração.

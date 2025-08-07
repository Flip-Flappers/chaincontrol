import CommandC2E_0
import BgeM3_1
import API_vague_selector_2
import API_TAG_selector_3
import API_target_selector_4
import API_target_show_5
import KeyWordsSelector
import KeyWords_refiner_0_3
import gradio as gr

import tools.ToolSelector as ToolSelector
import tools.DeviceTool as DeviceTool

keywordSelector = KeyWordsSelector.KeyWordsSelector()

def greet(command):

    think, answer, keywords = keywordSelector.select_keywords(command)
    toolSelector = ToolSelector.ToolSelector(keywords)
    think, answer, targetTool = toolSelector.select_tool(command)
    """if targetTool['toolName'] == "DeviceTool":
        deviceTool = DeviceTool.DeviceTool(keywords, keywords['deviceName'])
        think, answer, targetTool = deviceTool.intention_recognition(command)"""

    #keyWords_refiner = KeyWords_refiner_0_3.Command_Refine()
    #keyWords_refiner.refine_command()

    """
    bgeM3_1 = BgeM3_1.BgeM3_selector()
    bgeM3_1.main()
    
    api_selector_2 = API_vague_selector_2.API_vague_selector()
    api_selector_2.main()
    
    api_tag_selector = API_TAG_selector_3.API_TAG_selector()
    api_tag_selector.main()
    
    api_target_selector = API_target_selector_4.API_target_selector()
    api_target_selector.main()
    
    api_target_show = API_target_show_5.API_target_show()
    api_target_show.main()
    """

    return keywords, targetTool
def main():
    iface = gr.Interface(
        fn=greet,
        inputs=gr.Textbox(label="命令"),
        outputs=[
                    gr.JSON(label="targetDevice"),
                    gr.JSON(label="targetProduct")
                ],
        title="Gradio Demo",
        description="demo"
    )
    iface.launch()

# 主程序入口
if __name__ == "__main__":
    main()
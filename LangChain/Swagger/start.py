import CommandC2E_0
import BgeM3_1
import API_vague_selector_2
import API_TAG_selector_3
import API_target_selector_4
import API_target_show_5
import KeyWords_selector_0_1
import KeyWords_refiner_0_3

commandC2E_0 = CommandC2E_0.CommandC2E()
commandC2E_0.translate_command("帮我将设备2228888的温度调成42")

keyWords_selector = KeyWords_selector_0_1.KeyWords_selector()
keyWords_selector.main()

keyWords_refiner = KeyWords_refiner_0_3.Command_Refine()
keyWords_refiner.refine_command()

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
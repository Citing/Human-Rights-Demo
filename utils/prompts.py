import os
import yaml

class PromptManager:
    def __init__(self, config_path=None):
        if config_path is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            config_path = os.path.join(base_dir, "prompts.yaml")
        self.prompts = self.__load_prompts(config_path)
    
    def __load_prompts(self, config_path):
        with open(config_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file).get("prompts", {})
        
    def get_prompt(self, step, **kwargs):
        keys = step.split('.')
        template = self.prompts
        try:
            for key in keys:
                template = template[key]
        except KeyError:
            raise ValueError(f"Prompt template '{step}' not found.")
        
        return template.format(**kwargs)
import openai


def get_response(message_input):
    """
    Get response from openAI
    :param message_input:
    :return:
    """
    key = "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"
    openai.api_key = key

    response = openai.Completion.create(

        model="gpt-3.5-turbo",
        prompt=message_input,
        temperature=0.9,
        max_token=200,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["Human:", "AI:"]
    )

    choices = response.get("choices")
    choice_list = [choice.get("text").lstrip("\n") for choice in choices]

    return choice_list

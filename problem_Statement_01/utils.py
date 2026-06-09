from urllib.parse import urlparse, parse_qs


def extract_video_id(url):

    parsed_url = urlparse(url)

    # https://www.youtube.com/watch?v=abc123
    if parsed_url.hostname in [
        "www.youtube.com",
        "youtube.com"
    ]:

        return parse_qs(
            parsed_url.query
        ).get("v", [None])[0]

    # https://youtu.be/abc123
    elif parsed_url.hostname == "youtu.be":

        return parsed_url.path[1:]

    return None
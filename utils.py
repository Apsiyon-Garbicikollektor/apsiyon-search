import io
import pandas as pd


def convert_bytes_to_dataframe(content: bytes, content_type: str) -> pd.DataFrame:
    if content_type not in ("text/csv",):
        raise ValueError("unsupported file type")

    buffer = io.BytesIO(content)
    df = pd.read_csv(buffer)
    buffer.close()

    return df

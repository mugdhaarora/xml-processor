import pandas as pd
import xml.etree.ElementTree as et


def XML_parser(xmlroot, df_cols): 
    rows = []

    for node in xmlroot: 
        res = []
        #res.append(node.attrib.get(df_cols[0]))
        for element in df_cols[0:]: 
            if node is not None and node.attrib.get(element) is not None:
                res.append(node.attrib.get(element))
            else: 
                res.append(None)
        rows.append({df_cols[i]: res[i] 
                     for i, _ in enumerate(df_cols)})
    result_df = pd.DataFrame(rows, columns=df_cols)

    return result_df
    
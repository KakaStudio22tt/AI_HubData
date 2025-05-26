

# Hàm tổng quát để lọc sample theo label, tag hoặc object
def filter_samples(dataset, field, value, filter_type="label"):
    """
    Lọc samples trong dataset theo trường, giá trị và loại lọc.
    Args:
        dataset: FiftyOne dataset
        field: tên trường (ví dụ: 'ground_truth', 'tags', ...)
        value: giá trị cần lọc (ví dụ: 'bird', 'my_tag', ...)
        filter_type: 'label', 'tag', hoặc 'object'
    Returns:
        view: FiftyOne view đã lọc
    """
    
    from fiftyone import ViewField as F
    if filter_type == "label":
        view = dataset.filter_labels(field, F("label") == value)
    elif filter_type == "tag":
        view = dataset.match_tags([value])
    elif filter_type == "object":
        # Lọc theo object id hoặc thuộc tính khác của object
        view = dataset.filter_labels(field, F("id") == value)
    else:
        raise ValueError("filter_type không tồn tại")
    
    return view
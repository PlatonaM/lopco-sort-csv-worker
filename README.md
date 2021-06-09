## lopco-sort-csv-worker

Sorts the rows of a CSV file based on the contained timestamps.

### Configuration

`delimiter`: Delimiter used in the CSV file.

`time_column`: Column containing timestamps.

`time_format`: Use these [format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) when providing the timestamp format.

### Inputs

Type: single

`input_csv`: CSV file to sort.

### Outputs

Type: single

`output_csv`: Sorted CSV file.

### Description

    {
        "name": "Sort CSV",
        "image": "platonam/lopco-sort-csv-worker:latest",
        "data_cache_path": "/data_cache",
        "description": "Sort a Comma-Separated Values file.",
        "configs": {
            "delimiter": null,
            "time_column": null,
            "time_format": null
        },
        "input": {
            "type": "single",
            "fields": [
                {
                    "name": "input_csv",
                    "media_type": "text/csv",
                    "is_file": true
                }
            ]
        },
        "output": {
            "type": "single",
            "fields": [
                {
                    "name": "output_csv",
                    "media_type": "text/csv",
                    "is_file": true
                }
            ]
        }
    }

For the timestamp format as required by `time_format` please use these [format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).

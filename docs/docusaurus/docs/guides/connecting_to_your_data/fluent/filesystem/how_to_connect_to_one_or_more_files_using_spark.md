---
title: How to connect to one or more files using Spark
tag: [how-to, connect to data]
description: A brief how-to guide covering ...
keywords: [Great Expectations, Spark, Filesystem]
---

<!-- Import statements start here. -->
import Prerequisites from '/docs/components/_prerequisites.jsx'

<!-- Introduction -->
import Introduction from '/docs/components/connect_to_data/filesystem/_intro_connect_to_one_or_more_files_pandas_or_spark.mdx'

<!-- ### 1. Import GX and instantiate a Data Context -->
import ImportGxAndInstantiateADataContext from '/docs/components/setup/data_context/_import_gx_and_instantiate_a_data_context.md'

<!-- ### 2. Create a Datasource -->
import InfoFilesystemDatasourceRelativeBasePaths from '/docs/components/connect_to_data/filesystem/_info_filesystem_datasource_relative_base_paths.md'
import TipFilesystemDatasourceNestedSourceDataFolders from '/docs/components/connect_to_data/filesystem/_tip_filesystem_datasource_nested_source_data_folders.md'

<!-- ### 3. Add a Data Asset to the Datasource -->
import TipFilesystemDataAssetWhatIfBatchingRegexMatchesMultipleFiles from '/docs/components/connect_to_data/filesystem/_tip_filesystem_data_asset_if_batching_regex_matches_multiple_files.md'

<!-- ### 4. Repeat step 3 as needed -->
import DefiningMultipleDataAssets from '/docs/components/connect_to_data/filesystem/_defining_multiple_data_assets.md'

<!-- Next steps -->
import AfterCreateNonSqlDatasource from '/docs/components/connect_to_data/next_steps/_after_create_non_sql_datasource.md'

<Introduction execution_engine="Spark" />

## Prerequisites

<Prerequisites requirePython = {false} requireInstallation = {true} requireDataContext = {true} requireSourceData = {null} requireDatasource = {false} requireExpectationSuite = {false}>

- Access to source data stored in a filesystem

</Prerequisites> 

## Steps

### 1. Import the Great Expectations module and instantiate a Data Context

<ImportGxAndInstantiateADataContext />

### 2. Create a Datasource
A Filesystem Datasource can be created with two pieces of information:
- `name`: The name by which the Datasource will be referenced in the future
- `base_directory`: The path to the folder containing the files the Datasource will be used to connect to

In our example, we will define these in advance by storing them in the Python variables `datasource_name` and `path_to_folder_containing_csv_files`:

```python title="Python code"
datasource_name = "MyNewDatasource"
path_to_folder_containing_csv_files = "../taxi_data"
```

<InfoFilesystemDatasourceRelativeBasePaths />

Once we have determined our `name` and `base_directory`, we pass them in as parameters when we create our Datasource:

```python title = "Python code"
datasource = context.sources.add_spark_filesystem(name=datasource_name, base_path=path_to_folder_containing_csv_files)
```

<TipFilesystemDatasourceNestedSourceDataFolders />

### 3. Add a Data Asset to the Datasource

A Data Asset requires two pieces of information to be defined:
- `name`: The name by which you will reference the Data Asset (for when you have defined multiple Data Assets in the same Datasource)
- `batching_regex`: A regular expression that matches the files to be included in the Data Asset

<TipFilesystemDataAssetWhatIfBatchingRegexMatchesMultipleFiles />

For this example, we will define these two values in advance by storing them in the Python variables `asset_name` and (since we are connecting to NYC taxi data in this example) `batching_regex`:

```python title="Python code"
name = "my_taxi_data_asset"
batching_regex = "yellow_tripdata_sample_2023_01\.csv"
```

Once we have determined those two values, we will pass them in as parameters when we create our Data Asset:

```python title="Python code"
data_asset = datasource.add_csv_asset(
    name=name, batching_regex=batching_regex
)
```


### 4. Repeat step 3 as needed to add additional files as Data Assets

<DefiningMultipleDataAssets />

## Next steps

<AfterCreateNonSqlDatasource />

<!-- ## Additional information -->

<!-- TODO: Add this once we have a script.
### Code examples

To see the full source code used for the examples in this guide, please reference the following scripts in our GitHub repository:
- [script_name.py](https://path/to/the/script/on/github.com)
-->

<!-- TODO: Enable this and update links after the conceptual guides are revised
### Related reading

For more information on the concepts and reasoning employed by this guide, please reference the following informational guides:

- [What does a Datasource do behind the scenes?]
- [What are use the use cases for single vs multiple Batch Data Assets?]
-->
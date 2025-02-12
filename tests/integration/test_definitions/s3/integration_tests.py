from tests.integration.backend_dependencies import BackendDependencies
from tests.integration.integration_test_fixture import IntegrationTestFixture

s3_integration_tests = []

connecting_to_your_data = [
    IntegrationTestFixture(
        name="s3_pandas_inferred_and_runtime_yaml",
        user_flow_script="tests/integration/docusaurus/connecting_to_your_data/cloud/s3/pandas/inferred_and_runtime_yaml_example.py",
        data_context_dir="tests/integration/fixtures/no_datasources/great_expectations",
        backend_dependencies=[BackendDependencies.AWS],
    ),
    IntegrationTestFixture(
        name="s3_pandas_inferred_and_runtime_python",
        user_flow_script="tests/integration/docusaurus/connecting_to_your_data/cloud/s3/pandas/inferred_and_runtime_python_example.py",
        data_context_dir="tests/integration/fixtures/no_datasources/great_expectations",
        backend_dependencies=[BackendDependencies.AWS],
    ),
    IntegrationTestFixture(
        name="how_to_configure_an_inferredassetdataconnector",
        user_flow_script="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_an_inferredassetdataconnector.py",
        data_context_dir="tests/integration/fixtures/no_datasources/great_expectations",
        data_dir="tests/test_sets/dataconnector_docs",
        backend_dependencies=[BackendDependencies.AWS],
    ),
    IntegrationTestFixture(
        name="how_to_configure_a_configuredassetdataconnector",
        user_flow_script="tests/integration/docusaurus/connecting_to_your_data/how_to_configure_a_configuredassetdataconnector.py",
        data_context_dir="tests/integration/fixtures/no_datasources/great_expectations",
        data_dir="tests/test_sets/dataconnector_docs",
        backend_dependencies=[BackendDependencies.AWS],
    ),
    IntegrationTestFixture(
        name="s3_spark_inferred_and_runtime_yaml_example",
        user_flow_script="tests/integration/docusaurus/connecting_to_your_data/cloud/s3/spark/inferred_and_runtime_yaml_example.py",
        data_context_dir="tests/integration/fixtures/no_datasources/great_expectations",
        backend_dependencies=[BackendDependencies.SPARK, BackendDependencies.AWS],
    ),
    IntegrationTestFixture(
        name="s3_spark_inferred_and_runtime_python_example",
        user_flow_script="tests/integration/docusaurus/connecting_to_your_data/cloud/s3/spark/inferred_and_runtime_python_example.py",
        data_context_dir="tests/integration/fixtures/no_datasources/great_expectations",
        backend_dependencies=[BackendDependencies.SPARK, BackendDependencies.AWS],
    ),
]

deployment_patterns = [
    IntegrationTestFixture(
        name="deployment_pattern_pandas_s3",
        user_flow_script="tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_pandas.py",
        data_context_dir=None,
        backend_dependencies=[BackendDependencies.AWS],
    ),
    IntegrationTestFixture(
        name="deployment_pattern_spark_s3",
        user_flow_script="tests/integration/docusaurus/deployment_patterns/aws_cloud_storage_spark.py",
        data_context_dir=None,
        backend_dependencies=[BackendDependencies.AWS, BackendDependencies.SPARK],
    ),
]

split_data = []

sample_data = []

s3_integration_tests += connecting_to_your_data
s3_integration_tests += deployment_patterns
s3_integration_tests += split_data
s3_integration_tests += sample_data

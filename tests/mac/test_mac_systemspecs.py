import pytest
from inqry.system_specs import systemspecs

HW_TEST_DATA = {'Model Name': 'Mac Pro', 'Model Identifier': 'MacPro6,1', 'Processor Name': 'Quad-Core Intel Xeon E5',
                'Processor Speed': '3.7 GHz', 'Number of Processors': 1, 'Total Number of Cores': 4,
                'L2 Cache (per Core)': '256 KB', 'L3 Cache': '10 MB', 'Memory': '32 GB',
                'Boot ROM Version': 'MP61.0116.B21', 'SMC Version (system)': '2.20f18', 'Illumination Version': '1.4a6',
                'Serial Number (system)': 'F5KQH0P9F9VN', 'Hardware UUID': '4D4C19C7-19C4-5678-A936-A419C4609AFD'}

SYSTEM_SPECS = systemspecs.create_specs_from_system_profiler_hardware_output(HW_TEST_DATA)


def test_getting_value_from_key():
    assert HW_TEST_DATA.get('Boot ROM Version') == 'MP61.0116.B21'


def test_profile_instantiation_works():
    systemspecs.SystemSpecs(HW_TEST_DATA)


def test_operating_system_attribute():
    assert hasattr(SYSTEM_SPECS, "os_type")


def test_that_system_profile_object_has_storage_attribute():
    assert hasattr(SYSTEM_SPECS, "storage")


def test_that_system_profile_object_has_serial_attribute():
    assert hasattr(SYSTEM_SPECS, "serial")


def test_that_system_profile_object_has_cpu_name_attribute():
    assert hasattr(SYSTEM_SPECS, "cpu_name")


def test_that_system_profile_object_has_cpu_speed_attribute():
    assert hasattr(SYSTEM_SPECS, "cpu_speed")


def test_that_system_profile_object_has_cpu_processors_attribute():
    assert hasattr(SYSTEM_SPECS, "cpu_processors")


def test_system_profiler_has_os_type_attribute():
    assert bool(SYSTEM_SPECS.os_type) is True


def test_model_is_string():
    assert isinstance(SYSTEM_SPECS.model, str)


def test_serial_is_string():
    assert isinstance(SYSTEM_SPECS.serial, str)


def test_name_is_string():
    assert isinstance(SYSTEM_SPECS.cpu_name, str)


def test_processors_is_integer():
    assert isinstance(SYSTEM_SPECS.cpu_processors, int)


def test_speed_is_string():
    assert isinstance(SYSTEM_SPECS.cpu_speed, str)


def test_cores_is_integer():
    assert isinstance(SYSTEM_SPECS.cpu_cores, int)


@pytest.mark.skip
def test_when_ios_device_is_connected():
    pass


@pytest.mark.skip
def test_ability_to_get_components_from_system_profile_object():
    pass


@pytest.mark.skip
def test_collector_method_output_data_type_is_system_specs_class():
    assert isinstance(SYSTEM_SPECS.collector(), systemspecs.SystemSpecs)


@pytest.mark.skip
def test_if_disk_list_is_list():
    assert isinstance(SYSTEM_SPECS.storage(), list)

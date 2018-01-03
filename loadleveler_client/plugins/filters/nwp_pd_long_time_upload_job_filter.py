# coding=utf-8
import datetime
from nwpc_hpc_model.loadleveler.filter_condition import \
    PropertyFilterCondition, \
    create_less_value_checker, \
    create_in_value_checker, \
    create_equal_value_checker, \
    get_property_data
from nwpc_hpc_model.loadleveler.filter import Filter


filter_info = {
    'name': 'nwp_pd_long_time_upload_job_filter'
}


def get_datetime_data(job_item, property_id):
    result = get_property_data(job_item, property_id)
    # if property_id == 'llq.queue_date':
    #     result = datetime.datetime.strptime(result, "%Y-%m-%d %H:%M:%S")
    return result


def create_filter():
    query_date_condition = PropertyFilterCondition(
        "llq.queue_date",
        data_checker=create_less_value_checker(datetime.datetime.utcnow()-datetime.timedelta(hours=4)),
        data_parser=get_datetime_data
    )
    jobs_script_condition = PropertyFilterCondition(
        "llq.job_script",
        data_checker=create_in_value_checker('upload')
    )
    owner_condition = PropertyFilterCondition(
        "llq.owner",
        data_checker=create_equal_value_checker("nwp_pd")
    )

    a_filter = Filter()
    a_filter.conditions.append(owner_condition)
    a_filter.conditions.append(query_date_condition)
    a_filter.conditions.append(jobs_script_condition)

    return {
        'name': filter_info['name'],
        'filter': a_filter
    }
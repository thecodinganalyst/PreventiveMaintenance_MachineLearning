import pandas as pd

class PmTelemetry:
    
    data_path = "data/"
    telemetry_csv = data_path + "telemetry.csv"
    maint_csv = data_path + "maint.csv"
    machines_csv = data_path + "machines.csv"
    errors_csv = data_path + "errors.csv"
    failures_csv = data_path + "failures.csv"
    data = pd.DataFrame()
    
    def __init__(self):
        print("Read telemetry.csv")
        self.data = pd.read_csv(self.telemetry_csv, parse_dates=["datetime"])
    
    def merge_maint(self):
        self.merge_feature(self.maint_csv, ["datetime", "machineID"], ["datetime"])
    
    def merge_failures(self):
        self.merge_feature(self.failures_csv, ["datetime", "machineID"], ["datetime"])
    
    def merge_errors(self):
        self.merge_feature(self.errors_csv, ["datetime", "machineID"], ["datetime"])

    def merge_machines(self):
        print("Read and merge machines.csv")
        machines = pd.read_csv(self.machines_csv)
        self.data = self.data.merge(machines, how="left", on=["machineID"])
        del machines
        
    def gen_past_hr_rolling_telemetry(self, hr_count, col_postfix, aggfunc):
        print(f"Generate past {hr_count} hr rolling telemetry data aggregate by {aggfunc.__name__}")
        # Divide into dataframes grouped by machineID, and sort by datetime
        data_groups = {i: g for i, g in self.data.groupby("machineID")}
        for k in data_groups:
            data_groups[k].sort_values("datetime", inplace=True)
            # Create a new column for each feature, containing the mean of the values 
            # from the last 23 rows and current row. If there are less than 23 past 
            # rows, then just get the mean of whatever number of rows available
            data_groups[k][f"volt{col_postfix}"] = data_groups[k]["volt"].rolling(hr_count, min_periods=1).agg(aggfunc)
            data_groups[k][f"rotate{col_postfix}"] = data_groups[k]["rotate"].rolling(hr_count, min_periods=1).agg(aggfunc)
            data_groups[k][f"vibration{col_postfix}"] = data_groups[k]["vibration"].rolling(hr_count, min_periods=1).agg(aggfunc)  
            data_groups[k][f"pressure{col_postfix}"] = data_groups[k]["pressure"].rolling(hr_count, min_periods=1).agg(aggfunc)
        self.data = pd.concat(data_groups).reset_index().drop(["level_0", "level_1"], axis=1)
        del data_groups


    def merge_feature(self, csv_path, merge_fields, date_fields=None):
        print(f"Read and Merge feature {csv_path}")
        sub = pd.read_csv(csv_path, parse_dates=date_fields)
        sub = pd.get_dummies(sub)
        sub = sub.groupby(merge_fields).sum().reset_index()
        self.data = self.data.merge(sub, how="left", on=merge_fields)
        del sub
        self.data.fillna(0, inplace=True)
        
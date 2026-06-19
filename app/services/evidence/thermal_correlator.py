class ThermalCorrelator:

    def correlate(
        self,
        observations,
        thermal_findings
    ):

        mapping = {}

        for observation in observations:

            page = observation.page_number

            nearby = [
                finding
                for finding in thermal_findings
                if abs(
                    finding.page_number - page
                ) <= 2
            ]

            mapping[
                observation.observation_id
            ] = nearby

        return mapping

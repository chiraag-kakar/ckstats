import ckstats
chart = ckstats.new_chart()
ckstats.set_title(chart, "Wild Parrot Deaths per Year")
ckstats.set_x_axis(chart,
                   ["2009", "2010", "2011", "2012", "2013",
                    "2014", "2015"])
ckstats.set_y_axis(chart, minimum=0, maximum=700,
                   labels=[0, 100, 200, 300, 400, 500, 600, 700])
ckstats.set_series(chart, [250, 270, 510, 420, 680, 580, 450])
ckstats.set_series_type(chart, "bar")
ckstats.generate_chart(chart, "chart.pdf")

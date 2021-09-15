from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, HttpResponse
from django.views import View
from django.template.loader import render_to_string
def index(request):
    return render(request,'main/index.html')

def introduction(request):
    return render(request,'main/introduction_2.html')

def contect_us(request):
    return render(request,'main/contect_us.html')

def introduction_demo(request):
    return render(request,'main/introduction_demo.html')


# tot_dose = [ [0.0 for m in range(15)] for y in range(10)]
def cal_dose(index):
	tot_dose = [ [ 0.0 for m in range(15)] for y in range(10)]
	# print(index)
	tot_dose[0][0] = int(index['1_1'])*1.41
	tot_dose[0][1] = int(index['1_2'])*2.42
	tot_dose[0][2] = int(index['1_3'])*7.09
	tot_dose[0][3] = int(index['1_4'])*8.12
	tot_dose[0][4] = int(index['1_5'])*16.31
	tot_dose[0][5] = int(index['1_6'])*10.83
	tot_dose[0][6] = int(index['1_7'])*22.10
	tot_dose[0][7] = int(index['1_8'])*7.46
	tot_dose[0][8] = int(index['1_9'])*3.47
	tot_dose[0][9] = int(index['1_10'])*3.22
	tot_dose[0][10] = int(index['1_11'])*20.09

	tot_dose[1][0] = int(index['2_1'])*5.27
	tot_dose[1][1] = int(index['2_2'])*10.36
	tot_dose[1][2] = int(index['2_3'])*16.55
	tot_dose[1][3] = int(index['2_4'])*3.7
	tot_dose[1][4] = int(index['2_5'])*11.1
	# tot_dose[1][5] = int(index['2_6'])*10.83

	tot_dose[2][0] = int(index['3_1'])*12.71
	tot_dose[2][1] = int(index['3_2'])*54.35
	tot_dose[2][2] = int(index['3_3'])*5.2
	tot_dose[2][3] = int(index['3_4'])*4.56
	tot_dose[2][4] = int(index['3_5'])*69.66
	# tot_dose[2][5] = int(index['3_6'])*10.83

	tot_dose[3][0] = int(index['4_1'])*0.087
	tot_dose[3][1] = int(index['4_2'])*29.43
	tot_dose[3][2] = int(index['4_3'])*7.65
	tot_dose[3][3] = int(index['4_4'])*5.63
	tot_dose[3][4] = int(index['4_5'])*4.02
	# tot_dose[3][5] = int(index['4_6'])*10.83

	tot_dose[4][0] = int(index['5_1'])*3
	tot_dose[4][1] = int(index['5_2'])*8
	tot_dose[4][2] = int(index['5_3'])*6
	tot_dose[4][3] = int(index['5_4'])*6
	tot_dose[4][4] = int(index['5_5'])*6
	tot_dose[4][5] = int(index['5_6'])*1.2
	# tot_dose[4][6] = int(index['5_7'])*22.10


	tot_dose[5][0] = int(index['6_1'])*0.04
	tot_dose[5][1] = int(index['6_2'])*0.13
	tot_dose[5][2] = int(index['6_3'])*0.92
	tot_dose[5][3] = int(index['6_4'])*0.38
	tot_dose[5][4] = int(index['6_5'])*1.15
	tot_dose[5][5] = int(index['6_6'])*0.003
	# tot_dose[5][6] = int(index['6_7'])*22.1

	tot_dose[6][0] = int(index['7_1'])*0.39
	tot_dose[6][1] = int(index['7_2'])*0.59

	tot_dose[7][0] = int(index['8_1'])*0.0039
	tot_dose[7][1] = int(index['8_2'])*0.0057
	tot_dose[7][2] = int(index['8_3'])*0.0016
	tot_dose[7][3] = int(index['8_4'])*0.013
	tot_dose[7][4] = int(index['8_5'])*0.017
	tot_dose[7][5] = int(index['8_6'])*0.0022

	for i in range(8):

		# python tuple
		tot_dose[8][i]=round(sum(tot_dose[i]),3)
		tot_dose[9][0] = round(tot_dose[9][0]+sum(tot_dose[i]),4)
	# print('From cal_dose**************************')
	# print(tot_dose)
	# print(sum(tot_dose[0]))
	return tot_dose

from django.shortcuts import render

from plotly.offline import plot
import plotly.graph_objs as go

class Tool_View(View):
	template_name = 'main/tool.html'
	def __init__(self):
		super().__init__()

	def get(self, request):
		times_list = []
		for times in range(1,11):
			times_list.append(times)
		list_context = {'times_loop': times_list}
		return render(request, self.template_name,list_context)

	def post(self, request):
		times_list = []
		for times in range(1,11):
			times_list.append(times)
		list_context = {'times_loop': times_list}


		if request.method == "POST":
			tot_dose = cal_dose(request.POST)
			sum_dose=[ () for p in range(8) ]
			label_name = ['電腦斷層', '核子醫學', '心臟類攝影', '非心臟類攝影', '傳統透視攝影', '一般傳統X光', '乳房攝影', '牙科攝影']
			for t in range(8):
				sum_dose[t]=(tot_dose[8][t], label_name[t])

			sum_dose = (sorted(sum_dose, key = lambda sum_dose: sum_dose[0], reverse=True) )
			# sum_dose2 = (sorted(sum_dose, key = lambda sum_dose: sum_dose[0], reverse=True) )
			# tot_dose[8] = sorted( tot_dose[8], key = lambda tot_dose[8] : tot_dose[8][1])
			print(sum_dose)
			dose_quantity = []
			# dose_quantity2 = []
			for u in range(8):
				dose_quantity.append(sum_dose[u][0])
				# dose_quantity2.append(sum_dose2[u][0])
			xlabel=[]
			for k in range(8):
				xlabel.append(sum_dose[k][1])
			print(dose_quantity)
			sunflowers_colors = ['#f7e731', '#F4A7B9', '#E16B8C', '#66BAB7','#9B90C2', '#A5DEE4','#A8497A','#4E4F97']
			# sunflowers_colors_2 = [ '#4E4F97','#A8497A','#A5DEE4','#9B90C2', '#66BAB7','#E16B8C','#F4A7B9','#f7e731',]
			hist_data=(go.Histogram(
					x=dose_quantity,
					y=xlabel,
					histfunc="sum",
					name='experimental',
					xbins=dict(
						size=0.5,
						),
					marker_color=sunflowers_colors,
					opacity=0.75,
					orientation='h',

			))
			annotations = []
			for  yd, xd in zip( xlabel, dose_quantity):
				annotations.append(dict(xref='x1', yref='y1',
					y=yd, x=xd,
					text='                      '+str(xd)+' mSv',
					font=dict(family='Arial', size=14,
						color='#000000'),
					showarrow=False
				))
			hist_layout = go.Layout(
				# xaxis = {'title':'劑量 (毫西弗mSv)','showgrid':True,},
				template="xgridoff",
				# paper_bgcolor='rgba(0,0,0,0)',
				# plot_bgcolor='rgba(0,0,0,0)',
				xaxis=dict(
					showticklabels=False,
					side="top",
					# title='劑量 (毫西弗mSv)',
				),
				yaxis=dict(
					# showticklabels=False,

					# categoryorder='total ascending'
				),
				# yaxis = {'title':'項目', 'categoryorder':'total ascending'},
				bargap=0.2, # gap between bars of adjacent location coordinates
				bargroupgap=0.2, # gap between bars of the same location coordinates
				annotations=annotations
			)
			plot_hist = plot( {'data':[hist_data], 'layout':hist_layout }
			, auto_open=False, output_type='div', image_height=0.1)



			# sunflowers_colors = ['#F4A7B9', '#E16B8C', '#66BAB7','#9B90C2', '#A5DEE4','#A8497A','#4E4F97']
			plot_div = plot([go.Pie(labels=xlabel, values=dose_quantity,textinfo='none', name="劑量計算結果",marker_colors=sunflowers_colors )], auto_open=False, output_type='div',  image_height=0.1 )

			re_list = {'1th': tot_dose[8][0], '2th': tot_dose[8][1], '3th': tot_dose[8][2], '4th': tot_dose[8][3],'5th': tot_dose[8][4], '6th': tot_dose[8][5],  '7th': tot_dose[8][6], '8th':tot_dose[8][7], 'total_dose': tot_dose[9][0], 'plot_div': plot_div, 'plot_hist': plot_hist}
			rendered = render_to_string('main/response_user.html', re_list)
			return HttpResponse(rendered)

		return render(request, self.template_name,list_context)

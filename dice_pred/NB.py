from tensorflow.keras.models import load_model

def load_system(name):
    model = load_model(name) 
    # print('------------------------------------------------------------------------------------------------')
    # print('本程式為免費程式，公開於巴哈姆特好事989小屋創作禁止轉載')
    # print('網址:https://home.gamer.com.tw/artwork.php?sn=5361909')
    # print('程式更新請查看小屋 此版本為:V3.1.1')
    # print('準確率低下請前往小屋更新或回報')
    # print('------------------------------------------------------------------------------------------------')
    return model
    
    
def show_data(num):
    print('------------------------------------------------------------------------------------------------')
    data = [i for i in num]
    # return data
    print('當前數據為: {}'.format(data))
    
    
def turn_data(num):
    data = [int(i)-1 for i in num]
    
    return [data]

def get_weight_dis(num, model):
    predict = model.predict(num)
    weight = [[i+1,predict[0][i]] for i in range(6)]

    return weight

def get_weight(num):
    predict = model.predict(num)
    weight = [[i+1,predict[0][i]] for i in range(6)]

    return weight
    
    
def clc_weight(weight):
    weight = data_sort(weight)
    predict_score, manual_score = [0, 0, 0, 0], [0, 0, 0, 0]
    score = [10, 9, 8, 4, 3, 1]
    
    for cnt,data in enumerate(weight):
        num, p_w, m_w = data[0], data[1], score[cnt]
        if num % 2 == 0:
            manual_score[0] += m_w
            predict_score[0] += p_w
        else:
            manual_score[2] += m_w
            predict_score[2] += p_w
        if num >= 4:
            manual_score[1] += m_w
            predict_score[1] += p_w
        else:
            manual_score[3] += m_w
            predict_score[3] += p_w

    #print(manual_score)
    
    return manual_score, predict_score
    
   
def data_sort(data):
    weight = data[:]
    flag = 1
    while(flag):
        flag = 0
        for i in range(len(weight) - 1):
            if weight[i][1] < weight[i + 1][1]:
                tmp = weight[i]
                weight[i] = weight[i+1]
                weight[i + 1] = tmp
                flag = 1
                
    return weight
    
    
def show_result(manual_score, predict_score, data_weight):
    sort_num = data_sort(data_weight)
        
    # print('\n數字預測機率:',end='')
    predcit_num_stack = ''
    for cnt,data in enumerate(sort_num):
        if len(sort_num) == cnt+1:
            print(data[0])
            predcit_num_stack += str(data[0])
            
        else:
            print(data[0],'>',end=' ')
            predcit_num_stack += (str(data[0])+'>')
        
    weight = [i[1] for i in data_weight]
    num_index = weight.index(max(weight))
    print('\n程式預測數字:{}'.format(data_weight[num_index][0]),'\n')
    
    all_type = ['雙', '大', '單', '小']
    o_index = manual_score.index(max([manual_score[0],manual_score[2]]))
    bs_index = manual_score.index(max([manual_score[1],manual_score[3]]))
    p_index = predict_score.index(max(predict_score))

    print('單雙推薦下注:' + all_type[o_index],'\n')
    print('大小推薦下注:' + all_type[bs_index],'\n')
    print('程式預測下注:' + all_type[p_index],'\n')

    return predcit_num_stack, data_weight[num_index][0], all_type[o_index], all_type[bs_index], all_type[p_index]

#---------------------------------------------------------------------#

if __name__ == '__main__':
    model = load_system('model_num.h5')
    while(1):
        input_num = input('請輸入 6 筆數據:')
        
        if len(input_num)!=6:
            print('輸入錯誤請重新輸入!!')
            
        else:
            break


    while(1):
        show_data(input_num)
        data = turn_data(input_num)
        data_weight = get_weight(data)
        manual_score, predict_score,= clc_weight(data_weight)
        
        
        _, _, _, _, _=show_result(manual_score, predict_score, data_weight)
        
        while(1):
            n = input('\n實際數字:').split(' ')
            n = ''.join(n)
            if n=='' or int(n) > 6:
                print('輸入錯誤!!')
            else:
                input_num = input_num[1:6] + n
                break
    

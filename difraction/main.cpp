#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;

void load_from_file(const char* fname)
{
    ifstream in(fname);
}

int main()
{
    int lyambda, z;
    //cout << "Enter the wavelength, nm" << endl;
    //cin >> lyambda;
    //cout << "Enter the distance from the holes to the screen, m" << endl;
    //cin >> z;
    const int Size = 10; //ввели размер (сторону квадрата) одного пиксел€, клетки в mm!!!!

    int row,col;
    ifstream hel ("C://Users/Sergey/Desktop/difraction/Hello.txt");
    char word;
    if (!hel.is_open()) // если файл не открыт
        {
            cout << "‘айл не может быть открыт!\n"; // сообщить об этом
        }
    else
        {
        hel >> word;
        cout << word << endl;
        }
    ifstream fin ("painting.txt");
    fin>>row>>col;
    int ** data = new int * [row];
    for (int r = 0; r < row; r++)
    {
        data [r] = new int [col];
        for (int c = 0; c < col; c++)
        {
            fin >> data[r][c];
        }
    }
    fin.close();
    const double PI =  3.141592;
    int ** Re_G_table = new int * [row];
    int ** Im_G_table = new int * [row];
    for (int x = 0; x < row; x++)
    {
        for (int y = 0; y < col; y++)
        {
            int Re_Sum = 0;
            int Im_Sum = 0;
            for (int r = 0; r < row; r++)  // установили €чейку на экране, суммируем по преп€тствию
            {
                for (int c = 0; c < col; c++)
                {
                    int R = sqrt(pow(z,2)+pow((Size/1000)*(x-r),2)+pow((Size/1000)*(y-c),2));  // pow - возводит в квадрат
                    int cosinus = z/R;   // обозначен в лабнике cos(alpha)
                    int Re_per_Sum = data[r][c] * (cosinus/R) *cos(2*PI*pow(10,9)/(R*lyambda));
                    int Im_per_Sum = data[r][c] * (cosinus/R) *sin(2*PI*pow(10,9)/(R*lyambda)); // per - промежуточна€ сумма
                    Re_Sum += Re_per_Sum*pow((Size/1000),2);
                    Im_Sum += Im_per_Sum*pow((Size/1000),2);
                }
            }
            Re_G_table[x][y] = Re_Sum/lyambda;
            Im_G_table[x][y] = Im_Sum/lyambda;
        }
    }
    int ** intensive = new int * [row];
    for (int x = 0; x < row; x++)  // считаем интенсивности как квадрат модул€ g, учитыва€, что он комплексный
    {
        for (int y = 0; y < col; y++)
        {
            intensive[x][y] = pow(Re_G_table[x][y],2) + pow(Im_G_table[x][y],2);
        }
    }
    // далее делаем обрисовку. используем массив интенсивностей
    delete data;
    delete Re_G_table;
    delete Im_G_table;
    delete intensive;

    return 0;
}

# -*- coding:utf8 -*-
import cv2
import os
import time



def video2frame(video_path,saved_path,img_format='.jpg'):
    
    '''基本描述：
        @对指定文件夹下的所有视频进行抽帧处理，并将其保存在指定的目录当中

    Args:
        video_path(str): The path of the video which will be extract the frames.
        saved_path(str): path to save the extracted frames.If the savepath isn't exist,we will create the related folder.
    
    Returns:
        None

    Example:
        get_video_frame("./origin_video/","./origin_frame/")
    '''
    video_list = os.listdir(video_path)
    # 保存图片的帧率间隔
    for index, video_name in enumerate(video_list):
        video_path_ = os.path.join(video_path, video_name)
        img_folder = saved_path + video_name.split()[0]
        if not os.path.exists(img_folder):
            os.mkdir(img_folder)
        # 开始读视频
        videoCapture = cv2.VideoCapture(video_path_)
        print("正在处理第{}个视频，总共{}个视频".format(index+1, len(video_list)))
        while True:
            success, frame = videoCapture.read()
            if not success:
                print('video {} is all read'.format(video_name))
                break
            else:
                # 保存图片
                savedname = os.path.join(img_folder , str(j).zfill(7)+ img_format)
                cv2.imwrite(savedname, frame)
        videoCapture.release()

    return None


def frmae2video(image_folder,video_path,size,fps = 25,postfix='.jpg'):
    
    '''基本描述：
        @将指定文件夹下所有图像帧整合为一个视频

    Args:
        image_folder(str): The path of the frames folder.
        size(tuple(int,int)): size of thw image (h,w).
        fps(int): the frame rate of the synthetic video.

    Returns:
        None

    Example:
        picvideo(image_folder = r'../data_preprocess/save_image_check1',video_path = r"./res/" + "video1.mp4",size = (640,480),fps = 25)
    '''
    filelist = os.listdir(image_folder)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')#不同视频编码对应不同视频格式（例：'I','4','2','0' 对应avi格式）
    video = cv2.VideoWriter(video_path, fourcc, fps, size )
    for img_name in filelist:
        if img_name.endswith(postfix):
            img_path = os.ptah.join(img_path,img_name)
            img = cv2.imread(img_path)#opencv读取图像，直接通道顺序为BGR的numpy.ndarray对象，通道值默认范围0-255。
            video.write(img)
 
    video.release()

    return None


if __name__ == '__main__':

    pass



# -*- coding: utf-8 -*-
import sys, os
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import numpy as np
from PIL import Image

KHO_DIR = r"G:\My Drive\NotebookLM - Academic Knowledge Base\Cơ sở vật lý và công nghệ nano\Kho_Hinh_Anh"

sim_files = [
    ("[Mục 3.1 ĐT 1]", "[Mo_Phong]_Muc_3.1_The_Nang_Lennard_Jones_Va_Xap_Xi_Dieu_Hoa.png"),
    ("[Mục 3.1 ĐT 2]", "[Mo_Phong]_Muc_3.1_Mat_Do_Xac_Suat_Dao_Dong_Tu_Luong_Tu_Va_Co_Dien.png"),
    ("[Mục 3.1 ĐT 3]", "[Mo_Phong]_Muc_3.1_Dinh_Luat_Ti_Le_Tan_So_Theo_Kich_Thuoc.png"),
    ("[Mục 3.2 ĐT 1]", "[Mo_Phong]_Muc_3.2_Hang_So_Thoi_Gian_Nhiet_Va_Dinh_Luat_Ti_Le_L2.png"),
    ("[Mục 3.2 ĐT 2]", "[Mo_Phong]_Muc_3.2_Doi_Chuan_Van_Toc_Lang_Stokes_Va_Khuech_Tan_Brown.png"),
    ("[Mục 3.2 ĐT 3]", "[Mo_Phong]_Muc_3.2_The_Nang_Ma_Sat_Va_Hien_Tuong_Sieu_Tron_Incommensurate.png"),
    ("[Mục 3.3 ĐT 1]", "[Mo_Phong]_Muc_3.3_So_Sanh_Mat_Do_Trang_Thai_DOS_3D_2D_1D_0D.png"),
    ("[Mục 3.3 ĐT 2]", "[Mo_Phong]_Muc_3.3_Khe_Nang_Luong_Theo_Ban_Kinh_Cham_Luong_Tu_Model_Brus.png"),
    ("[Mục 3.3 ĐT 3]", "[Mo_Phong]_Muc_3.3_Phan_Loai_Vector_Chiral_Va_Khe_Nang_Luong_CNT.png"),
    ("[Mục 3.4 ĐT 1]", "[Mo_Phong]_Muc_3.4_Pho_Raman_Theo_Kich_Thuoc_Hat_Model_Fauchet.png"),
    ("[Mục 3.4 ĐT 2]", "[Mo_Phong]_Muc_3.4_Duong_Cong_Tu_Tre_Va_Chuyen_Pha_Sieu_Thuan_Tu.png"),
    ("[Mục 3.4 ĐT 3]", "[Mo_Phong]_Muc_3.4_Thoi_Gian_Hoi_Phuc_Neel_Va_Gioi_Han_Sieu_Thuan_Tu.png"),
    ("[Mục 3.5 ĐT 1]", "Mo_Phong_Muc_3.5_Do_Thi_01_Ty_So_Be_Mat_The_Tich.png"),
    ("[Mục 3.5 ĐT 2]", "Mo_Phong_Muc_3.5_Do_Thi_02_Coulomb_Blockade_SET.png"),
    ("[Mục 3.5 ĐT 3]", "Mo_Phong_Muc_3.5_Do_Thi_03_Pho_LSPR_Au_Ag.png"),
]

print("=" * 80)
print("KIỂM TOÁN HÌNH HỌC QUANG HỌC: KHOẢNG HỞ TIÊU ĐỀ - HỘP CHÚ GIẢI (15 ĐỒ THỊ)")
print("Tiêu chuẩn thiết kế: Khoảng cách thực tế >= 18.0 pt (Mục tiêu >= 20.0 pt)")
print("=" * 80)

all_passed = True
for tag, fname in sim_files:
    fpath = os.path.join(KHO_DIR, fname)
    if not os.path.exists(fpath):
        print(f"{tag:14s} | {fname:45s} | KHÔNG TÌM THẤY TỆP!")
        all_passed = False
        continue
    im = Image.open(fpath).convert("L")
    arr = np.array(im)
    
    # 1. Tìm đường viền ngang đỉnh của Legend (horizontal border run >= 200 px)
    leg_top = None
    for r in range(40, int(arr.shape[0] * 0.4)):
        row_line = arr[r, :]
        dark_run = np.max(np.diff(np.where(np.concatenate(([True], row_line > 200, [True])))[0]) - 1)
        if dark_run >= 200:
            leg_top = r
            break
            
    if leg_top is None:
        print(f"{tag:14s} | {fname:45s} | Không định vị được viền Legend!")
        all_passed = False
        continue
        
    # 2. Tìm điểm ảnh mực thấp nhất của tiêu đề nằm ngay phía trên viền Legend
    w = arr.shape[1]
    title_slice = arr[:leg_top, int(w * 0.15):int(w * 0.85)]
    ink_rows = np.where(np.any(title_slice < 200, axis=1))[0]
    if len(ink_rows) == 0:
        print(f"{tag:14s} | {fname:45s} | Không tìm thấy chữ tiêu đề!")
        all_passed = False
        continue
    title_bottom = ink_rows[-1]
    
    gap_px = leg_top - title_bottom
    gap_pt = gap_px * 72.0 / 300.0
    passed = gap_pt >= 18.0
    if not passed:
        all_passed = False
    status = "PASS (Hoàn hảo)" if gap_pt >= 20.0 else ("PASS" if passed else "FAIL (Quá sát)")
    print(f"{tag:14s} | Khoảng hở: {gap_px:3d} px ({gap_pt:4.1f} pt) | {status}")

print("=" * 80)
print(f"KẾT QUẢ TỔNG QUAN: {'100% ĐẠT CHUẨN HOÀN TOÀN' if all_passed else 'CẦN CHỈNH SỬA'}")
print("=" * 80)

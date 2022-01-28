import re

import pytest
import allure

from page_object.financial.financial_reimbursement import FinancialReimbursementApplication
from utils.logger import log
from utils.times import sleep

@allure.feature("测试财务报销申请")
@pytest.mark.run(order=2)
class TestFinancialReimbursement:

    @allure.story("成功发起财务报销申请")  #allure生成测试报告
    def test_financial_reimbursement(self, drivers):
        # 国内银行转账 差旅明细
        reimbursement = FinancialReimbursementApplication(drivers)
        reimbursement.click_work() #点击工作流
        reimbursement.click_my_work() #点击我的工作流
        reimbursement.click_add_work() #点击新建工作
        reimbursement.click_finance_category() #点击财务类
        reimbursement.click_financial_reimbursement_application('IGG 福州-203技术部-程序组-测试组-测试工程师') #点击财务报销申请
        reimbursement.switch_to_iframe_by_name('财务报销申请')
        reimbursement.switch_user('许晨欣','203技术部-程序组-测试组')
        reimbursement.select_company('福州天极数码有限公司')
        reimbursement.related_process_number_confirm()
        reimbursement.input_payment_time('2022-01-30')
        reimbursement.select_payment_currency('RMB')
        reimbursement.select_payment_method('银行转账')
        reimbursement.input_beneficiary_name('许晨欣')
        reimbursement.select_account_type('第三方账户')
        sleep(1)
        reimbursement.input_domestic_bank_city('福建省福州市')
        reimbursement.input_domestic_bank_name('招商银行')
        reimbursement.input_domestic_account_bank('福州分行东街口支行')
        reimbursement.input_domestic_beneficiary_account_name('测试')
        reimbursement.input_domestic_receiving_bank_account('1234567890')
        reimbursement.click_travel_details()
        reimbursement.click_travel_no_travel_allowance()
        sleep(2)
        reimbursement.input_travel_fee_type('住宿费','住宿费')
        reimbursement.input_travel_expense_vesting_period()
        reimbursement.input_travel_use('用途测试')
        reimbursement.select_travel_document_currency('USD')
        reimbursement.input_travel_pre_tax_amount('230')
        reimbursement.input_travel_taxi('5.00')
        reimbursement.input_remark('这是一条备注')
        reimbursement.click_approval_to_sponsor()
        reimbursement.click_dispatch_approver()
        reimbursement.click_set_steps('许晨欣')
        reimbursement.click_image_upload()
        reimbursement.click_turn_next()
        sleep(1)
        result = re.findall(r'提交成功', reimbursement.get_source)
        log.info(result)
        assert result
        reimbursement.click_confirm()


if __name__ == '__main__':
    pytest.main(["./TestCase/financial/test_financial_reimbursement.py"])







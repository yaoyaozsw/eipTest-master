#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from selenium.common.exceptions import TimeoutException

from common.readelement import Element
from config.conf import cm
from page_object.main_base_page import base
from page_object.financial.workflow import WorkPage
from utils.times import sleep, dt_strftime

financialReimbu = Element('financial_reimbursement')

class FinancialReimbursementApplication(WorkPage):

    def click_financial_reimbursement_application(self, functional_position):
        """点击财务报销申请"""
        self.is_click(financialReimbu['财务报销申请'])
        sleep(0.5)
        self.find_element_by_txt(financialReimbu['职能岗位_测试工程师'], functional_position,{'key': 'class', 'value': 'list-group-item'}).click()
        sleep(0.5)
        self.is_click(base['确认'])

    def select_company(self,company_name):
        self.select_item(financialReimbu['选择费用归属公司'], company_name)

    # def related_process_number_confirm(self,input_number,number):
    def related_process_number_confirm(self):
        """选择关联相关流程编号"""
        self.is_click(financialReimbu['关联相关流程编号'])
        #self.input_text(financialReimbu['关联相关流程编号输入框'], input_number)
        sleep(1.5)
        self.is_click(financialReimbu['关联相关流程编号选择无'])
        #self.find_element_by_txt(base['li'],number, {'key':'class','value':'select2-results-dept-0 select2-result select2-result-selectable select2-highlighted'}).click()

    def input_payment_time(self, time):
        """输入期望付款日期"""
        self.input_text(financialReimbu['期望付款日期'], time)

    def select_payment_currency(self, currency):
        """选择支付币种"""
        self.select_item(financialReimbu['选择支付币种'], currency)

    def select_payment_method(self, method):
        """选择支付方式"""
        self.select_item(financialReimbu['选择支付方式'], method)

    def input_beneficiary_name(self, name):
        """输入收款方姓名"""
        self.input_text(financialReimbu['收款方姓名'], name)

    def click_provide_proof(self):
        """点击是否需要出纳提供证明 是 """
        self.is_click(financialReimbu['需要出纳提供付款证明是'])

    def select_account_type(self, type):
        """选择账户类型"""
        self.select_item(financialReimbu['账户类型'], type)

    def input_receiving_account(self, account):
        """输入收款账号"""
        self.input_text(financialReimbu['收款账号'], account)

    def input_domestic_bank_city(self, city):
        """输入国内转账银行所在城市"""
        self.input_text(financialReimbu['国内转账银行所在城市'], city)

    def input_domestic_bank_name(self, name):
        """输入国内转账银行名称"""
        self.input_text(financialReimbu['国内转账银行名称'], name)

    def input_domestic_account_bank(self, bank):
        """输入国内转账开户行信息"""
        self.input_text(financialReimbu['国内转账开户行信息'], bank)

    def input_domestic_beneficiary_account_name(self, name):
        """输入国内转账收款人账户名称"""
        self.input_text(financialReimbu['国内转账收款人账户名称'], name)

    def input_domestic_receiving_bank_account(self, account):
        """输入国内转账收款银行账号"""
        self.input_text(financialReimbu['国内转账收款银行账号'], account)

    def input_foreign_beneficiary_account_name(self, name):
        """输入国外转账收款人账号名称"""
        self.input_text(financialReimbu['国外转账收款人账号名称'], name)

    def input_foreign_beneficiary_bank_account(self, account):
        """输入国外转账收款人银行账号"""
        self.input_text(financialReimbu['国外转账收款人银行账号'], account)

    def input_foreign_payee_address(self, address):
        """输入国外转账收款人地址"""
        self.input_text(financialReimbu['国外转账收款人地址'], address)

    def input_foreign_payee_telephone(self, telephone):
        """输入国外转账收款人电话"""
        self.input_text(financialReimbu['国外转账收款人电话'], telephone)

    def input_foreign_receiving_bank_name(self, name):
        """输入国外转账收款人银行名称"""
        self.input_text(financialReimbu['国外转账收款人银行名称'], name)

    def input_foreign_payee_bank_address(self, address):
        """输入国外转账收款人银行地址"""
        self.input_text(financialReimbu['国外转账收款人地址'], address)

    def input_foreign_payee_bank_swift_code(self, code):
        """输入国外转账收款人银行国际代码"""
        self.input_text(financialReimbu['国外转账收款人银行国际代码'], code)

    def input_foreign_payee_bank_remittance_code(self, code):
        """输入国外转账收款人银行汇款代码"""
        self.input_text(financialReimbu['国外转账收款人银行汇款代码'], code)

    def input_foreign_payee_bank_number(self, number):
        """输入国外转账收款人银行行号"""
        self.input_text(financialReimbu['国外转账收款人银行行号'], number)

    def input_foreign_payee_bank_branch_number(self, number):
        """输入国外转账收款人银行分行号"""
        self.input_text(financialReimbu['国外转账收款人银行分行号'], number)

    def click_travel_details(self):
        """点击差旅明细"""
        self.is_click(financialReimbu['差旅明细'])

    def click_travel_short_business_travel(self):
        """点击差旅短期出差"""
        self.is_click(financialReimbu['差旅短期出差'])

    def click_travel_no_travel_allowance(self):
        """点击差旅短期出差"""
        self.is_click(financialReimbu['差旅无出差补贴'])

    def click_travel_add_calculation(self):
        """点击差旅添加计算"""
        self.is_click(financialReimbu['差旅添加计算'])

    def click_travel_update_details(self):
        """点击差旅更新至费用明细"""
        self.is_click(financialReimbu['差旅更新至费用明细'])

    def click_travel_business_system(self):
        """点击差旅出差管理制度"""
        self.is_click(financialReimbu['差旅出差管理制度'])

    def click_travel_subsidy_description(self):
        """点击差旅长期出差补贴说明"""
        self.is_click(financialReimbu['差旅长期出差补贴说明'])

    def input_travel_fee_type(self, input_type,type):
        """选择差旅费用类型"""
        self.is_click(financialReimbu['差旅费用类型'])
        self.input_text(financialReimbu['差旅费用类型搜索框'],input_type)
        sleep(1.5)
        self.find_element_by_txt(base['li'],type, {'key': 'class', 'value': 'select2-results-dept-0 select2-result select2-result-selectable select2-highlighted'}).click()

    def input_travel_expense_vesting_period(self):
        """输入差旅费用归属期间"""
        self.is_click(financialReimbu['差旅费用归属期间'])
        self.is_click(financialReimbu['差旅费用归属期间2022'])
        self.is_click(financialReimbu['差旅费用归属期间202201'])
        self.is_click(financialReimbu['差旅费用归属期间20220114'])
        self.is_click(financialReimbu['差旅费用归属期间20220119'])
        self.is_click(financialReimbu['差旅费用归属期间apply'])

    def input_travel_use(self, use):
        """输入差旅税前金额"""
        self.input_text(financialReimbu['差旅用途'], use)

    def select_travel_document_currency(self, currency):
        """选择差旅单据币种"""
        self.select_item(financialReimbu['差旅单据币种'], currency)

    def input_travel_pre_tax_amount(self, amount):
        """输入差旅税前金额"""
        self.input_text(financialReimbu['差旅税前金额'], amount)

    def input_travel_taxi(self, taxi):
        """输入差旅税"""
        self.input_text(financialReimbu['差旅税'], taxi)

    def click_travel_delete(self):
        """点击差旅删除"""
        self.is_click(financialReimbu['差旅删除'])

    def click_travel_copy(self):
        """点击差旅复制"""
        self.is_click(financialReimbu['差旅复制'])

    def click_travel_Add_details(self):
        """点击差旅增加明细"""
        self.is_click(financialReimbu['差旅增加明细'])

    def click_travel_Calculate_total(self):
        """点击差旅计算总额"""
        self.is_click(financialReimbu['差旅计算总额'])

    def click_travel_USD_reference(self):
        """点击差旅USD参考"""
        self.is_click(financialReimbu['差旅USD参考'])

    def input_remark(self, remark):
        """输入差旅税"""
        self.input_text(financialReimbu['备注'], remark)

    def click_approval_to_sponsor(self):
        """点击出纳付款后，流程需审批到发起人，用于确认收款"""
        self.is_click(financialReimbu['出纳付款后流程需审批到发起人'])

    def click_dispatch_approver(self):
        """点击派发审批人"""
        self.is_click(financialReimbu['派发审批人按钮'])

    def click_set_steps(self,username):
        """点击设置审批步骤"""
        self.is_click(financialReimbu['设置审批步骤'])
        self.is_click(financialReimbu['设置审批步骤选择用户'])
        self.input_text(financialReimbu['选择用户输入关键词'], username)
        self.is_click(financialReimbu['选择用户点击查询'])
        self.is_click(financialReimbu['选择用户'])
        self.is_click(financialReimbu['选择用户确定'])
        self.is_click(financialReimbu['步骤确定'])

    def click_image_upload(self):
        """点击图片上传,并上传图片"""
        self.is_click(financialReimbu['点击选择文件'])
        self.upload(cm.image_file)
        sleep(1)
#        self.driver.switch_to.alert.accept()

    def click_turn_next(self):
        """点击提交"""
        self.is_click(financialReimbu['转交到下一步'])

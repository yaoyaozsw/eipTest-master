#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from common.readelement import Element
from page_object.main_base_page import BasePage, base

work = Element('workflow')


class WorkPage(BasePage):
    """工作流类"""

    def click_work(self):
        """点击工作流"""
        self.driver.switch_to.default_content()
        self.is_click(work['工作流'])

    def click_my_work(self):
        """点击我的工作流"""
        if not self.find_element(work['新建工作']).is_displayed():
            self.is_click(work['我的工作流'])

    def click_add_work(self):
        """点击新建工作"""
        self.is_click(work['新建工作'])

    def click_my_initiate_work(self):
        """点击我发起的工作"""
        self.is_click(work['我发起的工作'])

    def click_processed_work(self):
        """点击已处理工作"""
        self.is_click(work['已处理工作'])

    def click_processing_work(self):
        """点击待处理工作"""
        self.is_click(work['待处理工作'])

    def click_hr_category(self):
        """点击人事类"""
        self.switch_to_iframe_by_name('新建工作')
        self.is_click(work['人事类'])

    #44-51行  author：chenxinxu
    def click_finance_category(self):
        """点击财务类"""
        self.switch_to_iframe_by_name('新建工作')
        self.is_click(work['财务类'])

    def click_financial_reimbursement(self):
        """点击财务报销申请"""
        self.is_click(work['财务报销申请'])

    def click_apply_job_badge(self):
        """点击工牌补办申请"""
        self.is_click(work['工牌补办申请'])

    def click_induction_process(self):
        """点击IGG新人入职流程"""
        self.is_click(work['IGG新人入职流程'])

    def click_first_new_workflow(self):
        """点击我发起工作流中最新的一个申请"""
        self.is_click(work['我发起的首条数据'])

    def click_first_processed_workflow(self):
        """点击已处理工作最新的一个流程"""
        self.is_click(work['已处理工作首条数据'])

    def click_first_pending_workflow(self):
        """点击待处理工作最新的一个流程"""
        self.is_click(work['待处理工作首条数据'])

    def click_sign_for(self):
        """点击签收"""
        self.switch_to_last_iframe()
        self.is_click(base['签收'])
        self.click_confirm()

    def click_next_step(self):
        """点击转交到下一步"""
        self.is_click(work['转交到下一步'])


if __name__ == '__main__':
    pass

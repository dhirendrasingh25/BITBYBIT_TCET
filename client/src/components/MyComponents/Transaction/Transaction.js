import OrderTable from "pages/dashboard/OrdersTable";
import React from "react";

const Transaction = () => {
  return (
    <div>
      <div>
        <div className="flex flex-row">
          <div className="flex flex-col w-1/2 mr-4">
            <div className="text-md py-2 pl-2 text-[#4D5464] font-medium">
              Product Name
            </div>
            <input
              id="designation"
              type="text"
              placeholder="Product Name"
              className="text-[#667085] p-2 border  rounded-md"
            ></input>
          </div>
          <div className="flex flex-col w-1/2">
            <div className="text-md py-2 pl-2 text-[#4D5464] font-medium">
              Total Quantity
            </div>
            <input
              placeholder="Total Quantity"
              className="text-[#667085] p-2 border rounded-md"
            ></input>
          </div>
        </div>
        <div className="flex flex-row mt-2">
          <div className="flex flex-col w-1/2 mr-4">
            <div className="text-md py-2 pl-2 text-[#4D5464] font-medium">
              Status
            </div>
            <input
              id="designation"
              type="text"
              placeholder="Status"
              className="text-[#667085] p-2 border  rounded-md"
            ></input>
          </div>
          <div className="flex flex-col w-1/2">
            <div className="text-md py-2 pl-2 text-[#4D5464] font-medium">
              Total Amount
            </div>
            <input
              placeholder="Total Amount"
              className="text-[#667085] p-2 border rounded-md"
            ></input>
          </div>
        </div>
        <div className=" flex justify-end">
          <button
            type="button"
            className="p-2 px-3 rounded-lg text-white  font-semibold bg-black  mt-3"
          >
            Add Transaction +
          </button>
        </div>
      </div>
      <div className="text-lg font-medium py-2">Recent Transaction</div>
      <div className="border rounded-lg border-black">
        <OrderTable />
      </div>
    </div>
  );
};

export default Transaction;

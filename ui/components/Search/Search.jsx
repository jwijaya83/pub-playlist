import React from "react";
import "./Search.css";
import {debounce} from "lodash";

export const Search = ({onChange, delay}) => {
    const _debouncedOnChange = debounce(
            onChange,
            delay
        );

    const _handleInputChange = (e) => {
        _debouncedOnChange(e.target.value);
    }

    return (
        <div className="Search">
            <input type="text" onChange={_handleInputChange} placeholder="Enter your request..." className="search-query" autoFocus />
        </div>
    );
};
